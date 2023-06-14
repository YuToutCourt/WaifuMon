from player_script.player import Player
from npc_script.npc import NPC
from waifu.waifu import Waifu
from moves.move import Move
from random import uniform


class Fight:
    def __init__(self, player: Player, enemy: NPC):
        self.player = player
        self.enemy = enemy
        self.tour = 0

    def start(self):
        waifu_player = self.player.team[0]
        waifu_enemy = self.enemy.team[0]

        waifu_player.in_fight = True
        waifu_enemy.in_fight = True

        self.play_round(waifu_player, waifu_enemy)

    def play_round(self, waifu_player: Waifu, waifu_enemy: Waifu):
        self.tour += 1

        waifu_player.choice_move()
        self.enemy_choice(waifu_player, waifu_enemy)

        attacking_waifu, defending_waifu = self.determine_attack_order(
            waifu_player, waifu_enemy
        )

        self.attack(attacking_waifu, defending_waifu)

        if defending_waifu.pv <= 0:
            self.handle_knockout(defending_waifu)
            return

        self.play_round(defending_waifu, attacking_waifu)

    def determine_attack_order(self, waifu1: Waifu, waifu2: Waifu):
        if waifu1.move_to_use.priority == waifu2.move_to_use.priority:
            return sorted(
                [waifu1, waifu2], key=lambda waifu: waifu.vitesse, reverse=True
            )

        return sorted(
            [waifu1, waifu2], key=lambda waifu: waifu.move_to_use.priority, reverse=True
        )

    def attack(self, attacker: Waifu, defender: Waifu, stop=False):
        move_used = attacker.move_to_use

        if uniform(0, 100) <= move_used.accuracy:
            damage = self.calculate_damage(attacker, defender)
            defender.pv -= damage

            if defender.pv <= 0:
                self.handle_knockout(defender)
                return
        else:
            print("Le coup n'a pas touché")

        if stop: return
        self.attack(defender, attacker, stop=True)

    def handle_knockout(self, waifu: Waifu):
        waifu.KO = True
        waifu.in_fight = False

        # Make the player or the npc choose a new waifu
        if any(not waifu.KO for waifu in self.player.team):
            self.player.choice_next_waifu()

        else : 
            print("Player à perdu, le NPC a gagné")
            return

        if any(not waifu.KO for waifu in self.enemy.team):
            self.enemy_choice()

        else :
            print("NPC à perdu, le joueur a gagné")
            return

    def enemy_choice(self, waifu_player: Waifu, waifu_npc: Waifu):
        return self.npc.handle_choice_during_fight(waifu_player, waifu_npc)

    def __get_multiplier(self, attacker: Waifu, move_used: Move, opponent: Waifu):
        if any(attacker_type in opponent.types for attacker_type in attacker.types):
            multiplier = 1
        else:
            multiplier = 1.5

        if move_used.type in opponent.type.immunite:
            return 0

        for op_type in opponent.types:
            if move_used.type in op_type.faiblesse:
                multiplier *= 2

        for op_type in opponent.types:
            if move_used.type in op_type.resistance:
                multiplier /= 2

        if uniform(0, 100) <= 5.17:
            multiplier *= 1.5

        return multiplier

    def calculate_damage(self, attacker: Waifu, opponent: Waifu):
        move_used = attacker.move_to_use
        multiplier = self.__get_multiplier(attacker, move_used, opponent)

        damage = (
            ((2 * attacker.niveau + 10) / 250)
            * (attacker.attaque / opponent.defense)
            * move_used.power
            + 2
        ) * multiplier

        return damage

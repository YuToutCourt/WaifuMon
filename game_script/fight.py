from character.npc import NPC
from character.player import Player
from waifu.waifu import Waifu
from moves.move import Move
from random import uniform
from utils.log import log
from typing import Union


class Fight:
    def __init__(self, player: Player, npc: NPC):
        self.player = player
        self.npc = npc
        self.tour = 0
        self.finished = False

    def start(self):
        waifu_player = self.player.team[0]
        waifu_enemy = self.npc.team[0]

        waifu_player.in_fight = True
        waifu_enemy.in_fight = True

        self.play_round(waifu_player, waifu_enemy)

    def __check_team_waifu(self, waifu) -> Union[Player, NPC]:
        """
        Check in which team the waifu is
        :param waifu: Waifu to check
        :return: Player or NPC
        """
        for waifu_player in self.player.team:
            if waifu_player == waifu:
                return self.player
        
        for waifu_npc in self.npc.team:
            if waifu_npc == waifu:
                return self.npc
            
        raise Exception("Waifu not found in team")
        

    def play_round(self, waifu1: Waifu, waifu2: Waifu):
        log("Tour", self.tour)
        log("Current battle", f"{waifu1.name} vs {waifu2.name}")
        self.tour += 1

        obj = self.__check_team_waifu(waifu1)

        if isinstance(obj, Player):
            waifu1.display_pv()
            waifu2.display_pv()
            waifu1.choice_move()
            self.enemy_choice(waifu1, waifu2)
        else:
            waifu2.display_pv()
            waifu1.display_pv()
            waifu2.choice_move()
            self.enemy_choice(waifu2, waifu1)

        attacking_waifu, defending_waifu = self.determine_attack_order(waifu1, waifu2)

        self.attack(attacking_waifu, defending_waifu)

        if defending_waifu.hp <= 0:
            self.handle_knockout(defending_waifu)
            return

        self.play_round(attacking_waifu, defending_waifu)

    def determine_attack_order(self, waifu1: Waifu, waifu2: Waifu):
        if waifu1.move_to_use.priority == waifu2.move_to_use.priority:
            return sorted([waifu1, waifu2], key=lambda waifu: waifu.speed, reverse=True)

        return sorted(
            [waifu1, waifu2], key=lambda waifu: waifu.move_to_use.priority, reverse=True
        )

    def attack(self, attacker: Waifu, defender: Waifu, stop=False):
        move_used = attacker.move_to_use
        log("Attack", f"{attacker.name} use {move_used.name}")
        if uniform(0, 100) <= move_used.accuracy:
            damage = self.calculate_damage(attacker, defender)
            defender.hp -= damage

            if defender.hp <= 0:
                defender.display_pv()
                return self.handle_knockout(defender)
        else:
            print("Le coup n'a pas touché")

        if stop:
            return
        self.attack(defender, attacker, stop=True)

    def handle_knockout(self, waifu: Waifu):
        log(f"{waifu.name} est KO")
        waifu.KO = True
        waifu.in_fight = False

        # Make the player or the npc choose a new waifu
        if len(self.player.get_alive_waifu()) == 0:
            print("Player à perdu, le NPC a gagné")
            self.finished = True
            return

        elif self.player.get_waifu_in_fight() is None:
            self.player.choice_next_waifu()
            return self.play_round(
                self.player.get_waifu_in_fight(), self.npc.get_waifu_in_fight()
            )

        if len(self.npc.get_alive_waifu()) == 0:
            print("NPC à perdu, le Player a gagné")
            self.finished = True
            return

        elif self.npc.get_waifu_in_fight() is None:
            self.npc.choice_next_waifu()
            return self.play_round(
                self.player.get_waifu_in_fight(), self.npc.get_waifu_in_fight()
            )

    def enemy_choice(self, waifu_player: Waifu, waifu_npc: Waifu):
        return self.npc.handle_choice_during_fight(waifu_player, waifu_npc)

    def __get_multiplier(self, attacker: Waifu, move_used: Move, opponent: Waifu):
        if any(attacker_type in opponent.types for attacker_type in attacker.types):
            multiplier = 1
        else:
            multiplier = 1.5

        for type_ in opponent.types:
            if move_used.type == type_.immunities:
                print("C'est inefficace !")
                return 0

        for op_type in opponent.types:
            if move_used.type in op_type.weaknesses:
                print("C'est super efficace !")
                multiplier *= 2

        for op_type in opponent.types:
            if move_used.type in op_type.resistances:
                print("C'est pas très efficace...")
                multiplier /= 2

        if uniform(0, 100) <= 5.17:
            print("Coup critique !")
            multiplier *= 1.5

        return multiplier

    def calculate_damage(self, attacker: Waifu, opponent: Waifu):
        move_used = attacker.move_to_use
        if move_used.power == 0:
            return 0
        
        multiplier = self.__get_multiplier(attacker, move_used, opponent)

        damage = (
            ((2 * attacker.level + 10) / 250)
            * (attacker.attack / opponent.defense)
            * move_used.power
            + 2
        ) * multiplier

        return damage

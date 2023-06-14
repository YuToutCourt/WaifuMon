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

        # Display the waifu to the screen

        self.play_round(waifu_player, waifu_enemy)

    def play_round(self, waifu_player: Waifu, waifu_enemy: Waifu):
        self.tour += 1

        move_player = self.player_choice(waifu_player)
        move_enemy = self.enemy_choice(waifu_player, waifu_enemy)

        # Check for priority moves
        if move_player.priority > move_enemy.priority:
            pass




    def player_choice(self, waifu: Waifu):
        return waifu.choice_move()

    def enemy_choice(self, waifu_player: Waifu, waifu_npc: Waifu):
        return self.npc.handle_choice_during_fight(waifu_player, waifu_npc)

    def __get_multiplier(self, attacker: Waifu, move_used: Move, opponant: Waifu):
        # Check if waifu is STAB
        if any(attacker_type in opponant.types for attacker_type in attacker.types):
            multiplier = 1
        else:
            multiplier = 1.5

        # Check if waifu is immune to the move
        if move_used.type in opponant.type.immunite:
            return 0

        # Check if waifu is weak to the move
        for op_type in opponant.types:
            if move_used.type in op_type.faiblesse:
                multiplier *= 2

        # Check if waifu is resistant to the move
        for op_type in opponant.types:
            if move_used.type in op_type.resistance:
                multiplier /= 2

        # Critical hit
        if uniform(0, 100) <= 5.17:
            multiplier *= 1.5

        return multiplier

    def calculate_damage(self, attacker: Waifu, move_used: Move, opponant: Waifu):
        multiplier = self.__get_multiplier(attacker, move_used, opponant)

        damage = (
            ((2 * attacker.niveau + 10) / 250)
            * (attacker.attaque / opponant.defense)
            * move_used.power
            + 2
        ) * multiplier

        return damage

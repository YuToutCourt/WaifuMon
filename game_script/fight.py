from player_script.player import Player
from game_script.npc import NPC
from waifu.waifu import Waifu
from moves.move import Move
from random import uniform


class Fight:
    def __init__(self, player: Player, enemy: NPC):
        self.player = player
        self.enemy = enemy
        self.tour = 0

    def run(self):
        pass

    def player_turn(self):
        pass

    def enemy_turn(self):
        pass

    def end_fight(self):
        pass

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

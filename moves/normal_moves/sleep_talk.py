from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.status_enum import StatusE


class SleepTalk(Move):
    def __init__(self):
        super().__init__(
            "Sleep Talk",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        User performs one of its own moves while sleeping.
        """
        if waifu_user.status != StatusE.SLEEP:
            return

        from random import choice

        available_moves = [
            move
            for move in waifu_user.moves
            if move.pp > 0 and move.name != self.name and move.power > 0
        ]
        waifu_user.move_to_use = choice(available_moves)
        dmg = self.__calculate_damage(waifu_user, waifu_receiver)
        waifu_receiver.hp -= dmg
        log(self.name, waifu_user.name, f"used {waifu_user.move_to_use.name}")

    def __get_multiplier(self, attacker, move_used: Move, opponent):
        if any(move_used.type.type_name == type.type_name for type in attacker.types):
            multiplier = 1.5
        else:
            multiplier = 1

        for type_ in opponent.types:
            if move_used.type.type_name in type_.immunities:
                return 0

        for op_type in opponent.types:
            if move_used.type.type_name in op_type.weaknesses:
                multiplier *= 2

        for op_type in opponent.types:
            if move_used.type.type_name in op_type.resistances:
                multiplier /= 2

        return multiplier

    def __calculate_damage(self, attacker, opponent):
        move = attacker.move_to_use

        multiplier = self.__get_multiplier(attacker, move, opponent)
        damage = (
            ((2 * attacker.level + 10) / 250)
            * (attacker.attack / opponent.defense)
            * move.power
            + 2
        ) * multiplier

        return damage

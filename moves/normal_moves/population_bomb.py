from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from utils.animation import animation_damage

class PopulationBomb(Move):
    def __init__(self):
        super().__init__(
            "Population Bomb",
            type=TypeFactory.create_type(Types.NORMAL),
            power=20,
            accuracy=90,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Hits 1-10 times in a row.
        """
        from random import randint
        from time import sleep

        hits = randint(1, 10)
        for _ in range(hits - 1):
            dmg = self.__calculate_damage(waifu_user, waifu_receiver)
            animation_damage(waifu_receiver, dmg)
            log(self.name, waifu_receiver.name, f"lost {dmg} hp")
            sleep(1)

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
        multiplier = self.__get_multiplier(attacker, self, opponent)
        damage = (
            ((2 * attacker.level + 10) / 250)
            * (attacker.attack / opponent.defense)
            * self.power
            + 2
        ) * multiplier

        return damage

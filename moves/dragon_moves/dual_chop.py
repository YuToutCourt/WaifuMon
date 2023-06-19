from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class DualChop(Move):
    def __init__(self):
        super().__init__(
            "Dual Chop",
            type=TypeFactory.create_type(Types.DRAGON),
            power=40,
            accuracy=90,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Hits twice in one turn.
        """
        damage = self.__calculate_damage(waifu_user, waifu_receiver)
        log(self.name, "dealt", damage, "damage to", waifu_receiver.name)
        waifu_receiver.hp -= damage

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

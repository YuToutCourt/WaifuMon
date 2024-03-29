from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class TrumpCard(Move):
    def __init__(self):
        super().__init__(
            "Trump Card",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        The lower the PP, the higher the power.
        5 	40
        4	50
        3	60
        2	80
        1	200
        """
        if self.pp == 5:
            self.power = 40
        elif self.pp == 4:
            self.power = 50
        elif self.pp == 3:
            self.power = 60
        elif self.pp == 2:
            self.power = 80
        elif self.pp == 1:
            self.power = 200

        damage = self.__calculate_damage(waifu_user, waifu_receiver)
        waifu_receiver.hp -= damage
        log(self.name, waifu_receiver.name, f"lost {damage} HP")

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

from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from utils.animation import animation_damage

class TripleKick(Move):
    def __init__(self):
        super().__init__(
            "Triple Kick",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=10,
            accuracy=90,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Hits thrice in one turn at increasing power.
        """
        from time import sleep
        
        for _ in range(2):
            self.power *= 3
            damage = self.__calculate_damage(waifu_user, waifu_receiver)
            animation_damage(waifu_receiver, damage)
            log(
                self.name,
                f"{waifu_user.name} inflicted {damage} damage to {waifu_receiver.name}",
            )
            sleep(1)

        self.power = 10

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

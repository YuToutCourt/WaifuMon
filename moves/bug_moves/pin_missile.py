from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class PinMissile(Move):
    def __init__(self):
        super().__init__(
            "Pin Missile",
            type=TypeFactory.create_type(Types.BUG),
            power=25,
            accuracy=95,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Hits 2-5 times in one turn.
        """
        from random import randint
        hits = randint(2, 5)
        for _ in range(hits-1):
            dmg = self.__calculate_damage(waifu_user, waifu_receiver)
            waifu_receiver.hp -= dmg
            log(self.name, waifu_receiver.name, f"lost {dmg} HP")

    def __get_multiplier(self, attacker, move_used: Move, opponent):
            from random import uniform
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

            if uniform(0, 100) <= 5.17:
                log("Coup critique !")
                multiplier *= 1.5

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


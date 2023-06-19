from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class Present(Move):
    def __init__(self):
        super().__init__(
            "Present",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=90,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Either deals damage or heals.
        power de 40	40%
        power de 80	30%
        power de 120	10%
        Heal 80 HP de la cible 20%
        """
        from random import randint

        if randint(1, 100) <= 40:
            self.power = 40
        elif randint(1, 100) <= 30:
            self.power = 80
        elif randint(1, 100) <= 10:
            self.power = 120
        else:
            self.power = 0

        if self.power == 0:
            heal = waifu_receiver.hp_max * 0.2
            if waifu_receiver.hp + heal > waifu_receiver.hp_max:
                waifu_receiver.hp = waifu_receiver.hp_max
            else:
                waifu_receiver.hp += heal
                log(f"{waifu_receiver.name} healed {heal} HP")

        else:
            dmg = self.__calculate_damage(waifu_user, waifu_receiver)
            waifu_receiver.hp -= dmg
            log(f"{waifu_receiver.name} took {dmg} damage")


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
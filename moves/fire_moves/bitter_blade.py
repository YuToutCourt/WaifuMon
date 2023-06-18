from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class BitterBlade(Move):
    def __init__(self):
        super().__init__(
            "Bitter Blade",
            type=TypeFactory.create_type(Types.FIRE),
            power=90,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        User recovers random HP .
        """
        from random import randint
        hp = randint(20, 200)
        waifu_user.hp += hp
        if waifu_user.hp > waifu_user.hp_max:
            waifu_user.hp = waifu_user.hp_max
        log("Bitter Blade", f"{waifu_user.name} recovered {hp} HP")

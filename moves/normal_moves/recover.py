from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class Recover(Move):
    def __init__(self):
        super().__init__(
            "Recover",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        User recovers half its max HP.
        """
        heal = waifu_user.hp_max / 2
        if waifu_user.hp + heal > waifu_user.hp_max:
            waifu_user.hp = waifu_user.hp_max
        else:
            waifu_user.hp += heal
        log(f"{waifu_user.name} recovered {heal} HP!")

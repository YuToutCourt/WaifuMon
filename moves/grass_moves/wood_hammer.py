from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class WoodHammer(Move):
    def __init__(self):
        super().__init__(
            "Wood Hammer",
            type=TypeFactory.create_type(Types.GRASS),
            power=120,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        User receives recoil damage.
        """
        waifu_user.hp -= waifu_user.hp_max * 0.25
        log("WoodHammer", f"{waifu_user.name} is hurt by recoil !")

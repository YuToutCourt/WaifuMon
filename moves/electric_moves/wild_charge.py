from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class WildCharge(Move):
    def __init__(self):
        super().__init__(
            "Wild Charge",
            type=TypeFactory.create_type(Types.ELECTRIC),
            power=90,
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
        log("WildCharge", f"{waifu_user.name} is hurt by recoil !")
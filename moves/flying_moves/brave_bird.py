from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log

class BraveBird(Move):
    def __init__(self):
        super().__init__(
            "Brave Bird",
            type=TypeFactory.create_type(Types.FLYING),
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
        waifu_user.hp -= waifu_user.max_hp * 0.25
        log("BraveBird", f"{waifu_user.name} is hurt by recoil !")

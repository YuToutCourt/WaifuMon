from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log


class DoubleEdge(Move):
    def __init__(self):
        super().__init__(
            "Double-Edge",
            type=TypeFactory.create_type(Types.NORMAL),
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
        log("Double-Edge", f"{waifu_user.name} is hurt by recoil !")

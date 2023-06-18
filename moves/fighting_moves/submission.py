from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.log import log

class Submission(Move):
    def __init__(self):
        super().__init__(
            "Submission",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=80,
            accuracy=80,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_reciver):
        """
        User receives recoil damage.
        """
        waifu_user.hp -= waifu_user.hp_max * 0.25
        log("Submission", f"{waifu_user.name} is hurt by recoil !")

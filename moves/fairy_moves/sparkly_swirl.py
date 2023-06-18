from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class SparklySwirl(Move):
    def __init__(self):
        super().__init__(
            "Sparkly Swirl",
            type=TypeFactory.create_type(Types.FAIRY),
            power=90,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Cures all status problems.
        """
        if waifu_user.status is None:
            log(waifu_user.name, "is not affected by any status")
        else:
            waifu_user.status = None
            log(waifu_user.name, "remove every status")

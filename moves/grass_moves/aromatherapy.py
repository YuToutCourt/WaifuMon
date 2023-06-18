from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class Aromatherapy(Move):
    def __init__(self):
        super().__init__(
            "Aromatherapy",
            type=TypeFactory.create_type(Types.GRASS),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Cures all status problems.
        """
        waifu_user.status = None
        log(waifu_user.name, "is cured from status problem")

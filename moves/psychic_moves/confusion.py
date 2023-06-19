from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.confuse import Confusion

class Confusion(Move):
    def __init__(self):
        super().__init__(
            "Confusion",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=50,
            accuracy=100,
            pp=25,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May confuse opponent.
        """
        if waifu_receiver.status is not None:
            log("But it failed")
            return
        waifu_receiver.status = Confusion(waifu_receiver, False)
        log(self.name, waifu_receiver.name, "was confused")

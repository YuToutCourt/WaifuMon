from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.confuse import Confusion

class Supersonic(Move):
    def __init__(self):
        super().__init__(
            "Supersonic",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=55,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Confuses opponent.
        """
        if waifu_receiver.status is None:
            waifu_receiver.status = Confusion(waifu_receiver, False)
            log(self.name, waifu_receiver.name, "is confused")
        else:
            log(self.name, waifu_receiver.name, "failed")

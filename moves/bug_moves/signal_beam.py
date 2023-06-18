from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.confuse import Confusion

class SignalBeam(Move):
    def __init__(self):
        super().__init__(
            "Signal Beam",
            type=TypeFactory.create_type(Types.BUG),
            power=75,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=10,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May confuse opponent.
        """
        if not waifu_receiver.status is None:
            waifu_receiver.status = Confusion(waifu_receiver, False)
            log(self.name, waifu_receiver.name, "is confused")
        else:
            log(self.name, waifu_receiver.name, "is already confused")

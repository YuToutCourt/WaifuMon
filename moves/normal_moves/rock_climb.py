from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.confuse import Confusion

class RockClimb(Move):
    def __init__(self):
        super().__init__(
            "Rock Climb",
            type=TypeFactory.create_type(Types.NORMAL),
            power=90,
            accuracy=85,
            pp=20,
            priority=0,
            proba_effect=20,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May confuse opponent.
        """
        if waifu_receiver.status is None:
            waifu_receiver.status = Confusion()
            log(self.name, waifu_receiver.name, "is confused")
        else:
            log(self.name, waifu_receiver.name, "is already confused")
        

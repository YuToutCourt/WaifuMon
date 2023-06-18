from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.confuse import Confusion

class Hurricane(Move):
    def __init__(self):
        super().__init__(
            "Hurricane",
            type=TypeFactory.create_type(Types.FLYING),
            power=110,
            accuracy=70,
            pp=10,
            priority=0,
            proba_effect=30,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May confuse opponent.
        """
        if waifu_receiver.status is None:
            waifu_receiver.status = Confusion(waifu_receiver, False)
            log(self.name, waifu_receiver.name, "is confused")
        else:
            log(self.name, waifu_receiver.name, "have already a status effect")

from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.confuse import Confusion

class TeeterDance(Move):
    def __init__(self):
        super().__init__(
            "Teeter Dance",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Confuses all Pokemon.
        """
        if waifu_receiver.status is not None:
            log("But it failed")
            return
        waifu_receiver.status = Confusion(waifu_receiver, False)
        log(self.name, waifu_receiver.name, "became confused")

        if waifu_user.status is not None:
            log("But it failed")
            return
        waifu_user.status = Confusion(waifu_user, False)
        log(self.name, waifu_user.name, "became confused")


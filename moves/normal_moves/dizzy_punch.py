from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.confuse import Confusion


class DizzyPunch(Move):
    def __init__(self):
        super().__init__(
            "Dizzy Punch",
            type=TypeFactory.create_type(Types.NORMAL),
            power=70,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=20,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May confuse opponent.
        """
        if waifu_receiver.status is None:
            waifu_receiver.status = Confuse(waifu_receiver, False)
            log(self.name, "confused", waifu_receiver.name)
        else:
            log(waifu_receiver.name, "is already confused")

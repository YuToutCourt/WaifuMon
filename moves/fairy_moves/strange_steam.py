from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.confuse import Confusion


class StrangeSteam(Move):
    def __init__(self):
        super().__init__(
            "Strange Steam",
            type=TypeFactory.create_type(Types.FAIRY),
            power=90,
            accuracy=95,
            pp=10,
            priority=0,
            proba_effect=20,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May confuse opponent.
        """
        if waifu_receiver.status is not None:
            log(waifu_receiver.name, "is already", waifu_receiver.status.name)
        else:
            waifu_receiver.status = Confusion(waifu_receiver, False)
            log(self.name, waifu_receiver.name, "is confused")

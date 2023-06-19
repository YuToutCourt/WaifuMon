from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from status.paralysis import Paralysis
from utils.logger import log


class Glare(Move):
    def __init__(self):
        super().__init__(
            "Glare",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=30,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Paralyzes opponent.
        """
        if waifu_receiver.status is None:
            waifu_receiver.status = Paralysis(waifu_receiver, False)
            log(self.name, "paralyzed", waifu_receiver.name)
        else:
            log(waifu_receiver.name, "is already paralyzed")

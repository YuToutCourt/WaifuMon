from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.paralysis import Paralysis


class WildboltStorm(Move):
    def __init__(self):
        super().__init__(
            "Wildbolt Storm",
            type=TypeFactory.create_type(Types.ELECTRIC),
            power=100,
            accuracy=80,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        May paralyze target.
        """
        if waifu_receiver.status is not None:
            log(waifu_receiver.name, "is already", waifu_receiver.status.status)
        else:
            waifu_receiver.status = Paralysis(waifu_receiver, False)
            log(self.name, waifu_receiver.name, "is paralyzed")

from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log
from status.paralysis import Paralysis

class BuzzyBuzz(Move):
    def __init__(self):
        super().__init__(
            "Buzzy Buzz",
            type=TypeFactory.create_type(Types.ELECTRIC),
            power=90,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        Paralyzes the opponent.
        """
        if waifu_receiver.status is not None:
            log(waifu_receiver.name, "is already", waifu_receiver.status.name)
        else:
            waifu_receiver.status = Paralysis(waifu_receiver, False)
            log(self.name, waifu_receiver.name, "is paralyzed")

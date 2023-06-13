from .move import Move
from waifu_types.type import Type

class HeartStamp(Move):
    def __init__(self):
        super().__init__("Heart Stamp", type=Type.PSYCHIC, power=60, accuracy=100, pp=25, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass

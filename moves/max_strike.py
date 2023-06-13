from .move import Move
from waifu_types.type import Type

class MaxStrike(Move):
    def __init__(self):
        super().__init__("Max Strike", type=Type.NORMAL, power=0, accuracy=100, pp=—, proba_effect=100)

    def effect(self):
        """
        Normal type Dynamax move. Lowers the target's Speed.
        """
        pass

from .move import Move
from waifu_types.type import Type

class Kinesis(Move):
    def __init__(self):
        super().__init__("Kinesis", type=Type.PSYCHIC, power=0, accuracy=80, pp=15, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Accuracy.
        """
        pass

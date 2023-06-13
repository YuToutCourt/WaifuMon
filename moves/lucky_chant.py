from .move import Move
from waifu_types.type import Type

class LuckyChant(Move):
    def __init__(self):
        super().__init__("Lucky Chant", type=Type.NORMAL, power=0, accuracy=100, pp=30, proba_effect=100)

    def effect(self):
        """
        Opponent cannot land critical hits for 5 turns.
        """
        pass

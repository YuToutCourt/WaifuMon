from .move import Move
from waifu_types.type import Type

class HelpingHand(Move):
    def __init__(self):
        super().__init__("Helping Hand", type=Type.NORMAL, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        In Double Battles, boosts the power of the partner's move.
        """
        pass

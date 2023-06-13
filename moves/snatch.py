from .move import Move
from waifu_types.type import Type

class Snatch(Move):
    def __init__(self):
        super().__init__("Snatch", type=Type.DARK, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Steals the effects of the opponent's next move.
        """
        pass

from .move import Move
from waifu_types.type import Type

class CourtChange(Move):
    def __init__(self):
        super().__init__("Court Change", type=Type.NORMAL, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Swaps the effects on either side of the field.
        """
        pass

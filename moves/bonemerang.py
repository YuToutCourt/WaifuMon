from .move import Move
from waifu_types.type import Type

class Bonemerang(Move):
    def __init__(self):
        super().__init__("Bonemerang", type=Type.GROUND, power=50, accuracy=90, pp=10, proba_effect=100)

    def effect(self):
        """
        Hits twice in one turn.
        """
        pass

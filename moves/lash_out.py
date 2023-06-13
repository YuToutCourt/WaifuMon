from .move import Move
from waifu_types.type import Type

class LashOut(Move):
    def __init__(self):
        super().__init__("Lash Out", type=Type.DARK, power=75, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Double power if stats were lowered during the turn.
        """
        pass

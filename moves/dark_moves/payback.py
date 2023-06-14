from ..move import Move
from waifu_types.type import Type

class Payback(Move):
    def __init__(self):
        super().__init__("Payback", type=Type.DARK, power=50, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Power doubles if the user was attacked first.
        """
        pass

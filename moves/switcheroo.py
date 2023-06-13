from .move import Move
from waifu_types.type import Type

class Switcheroo(Move):
    def __init__(self):
        super().__init__("Switcheroo", type=Type.DARK, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Swaps held items with the opponent.
        """
        pass

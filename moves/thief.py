from .move import Move
from waifu_types.type import Type

class Thief(Move):
    def __init__(self):
        super().__init__("Thief", type=Type.DARK, power=60, accuracy=100, pp=25, proba_effect=100)

    def effect(self):
        """
        Also steals opponent's held item.
        """
        pass

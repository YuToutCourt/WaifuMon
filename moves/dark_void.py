from .move import Move
from waifu_types.type import Type

class DarkVoid(Move):
    def __init__(self):
        super().__init__("Dark Void", type=Type.DARK, power=0, accuracy=50, pp=10, proba_effect=100)

    def effect(self):
        """
        Puts all adjacent opponents to sleep.
        """
        pass

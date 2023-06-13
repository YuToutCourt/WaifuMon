from .move import Move
from waifu_types.type import Type

class DazzlingGleam(Move):
    def __init__(self):
        super().__init__("Dazzling Gleam", type=Type.FAIRY, power=80, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Hits all adjacent opponents.
        """
        pass

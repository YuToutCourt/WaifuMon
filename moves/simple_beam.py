from .move import Move
from waifu_types.type import Type

class SimpleBeam(Move):
    def __init__(self):
        super().__init__("Simple Beam", type=Type.NORMAL, power=0, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Changes target's ability to Simple.
        """
        pass

from .move import Move
from waifu_types.type import Type

class Nature'sMadness(Move):
    def __init__(self):
        super().__init__("Nature's Madness", type=Type.FAIRY, power=0, accuracy=90, pp=10, proba_effect=100)

    def effect(self):
        """
        Halves the foe's HP.
        """
        pass

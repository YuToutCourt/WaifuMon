from .move import Move
from waifu_types.type import Type

class FocusBlast(Move):
    def __init__(self):
        super().__init__("Focus Blast", type=Type.FIGHTING, power=120, accuracy=70, pp=5, proba_effect=10)

    def effect(self):
        """
        May lower opponent's Special Defense.
        """
        pass

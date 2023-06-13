from .move import Move
from waifu_types.type import Type

class MirrorShot(Move):
    def __init__(self):
        super().__init__("Mirror Shot", type=Type.STEEL, power=65, accuracy=85, pp=10, proba_effect=30)

    def effect(self):
        """
        May lower opponent's Accuracy.
        """
        pass

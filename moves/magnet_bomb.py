from .move import Move
from waifu_types.type import Type

class MagnetBomb(Move):
    def __init__(self):
        super().__init__("Magnet Bomb", type=Type.STEEL, power=60, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Ignores Accuracy and Evasiveness.
        """
        pass

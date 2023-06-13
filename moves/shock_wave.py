from .move import Move
from waifu_types.type import Type

class ShockWave(Move):
    def __init__(self):
        super().__init__("Shock Wave", type=Type.ELECTRIC, power=60, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Ignores Accuracy and Evasiveness.
        """
        pass

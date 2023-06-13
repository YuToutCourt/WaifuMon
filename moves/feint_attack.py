from .move import Move
from waifu_types.type import Type

class FeintAttack(Move):
    def __init__(self):
        super().__init__("Feint Attack", type=Type.DARK, power=60, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Ignores Accuracy and Evasiveness.
        """
        pass

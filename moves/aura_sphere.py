from .move import Move
from waifu_types.type import Type

class AuraSphere(Move):
    def __init__(self):
        super().__init__("Aura Sphere", type=Type.FIGHTING, power=80, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Ignores Accuracy and Evasiveness.
        """
        pass

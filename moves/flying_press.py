from .move import Move
from waifu_types.type import Type

class FlyingPress(Move):
    def __init__(self):
        super().__init__("Flying Press", type=Type.FIGHTING, power=100, accuracy=95, pp=10, proba_effect=100)

    def effect(self):
        """
        Deals Fighting and Flying type damage.
        """
        pass

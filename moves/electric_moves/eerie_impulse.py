from ..move import Move
from waifu_types.type import Type

class EerieImpulse(Move):
    def __init__(self):
        super().__init__("Eerie Impulse", type=Type.ELECTRIC, power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply lowers opponent's Special Attack.
        """
        pass

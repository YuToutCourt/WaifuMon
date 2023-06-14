from ..move import Move
from waifu_types.type import Type

class ParabolicCharge(Move):
    def __init__(self):
        super().__init__("Parabolic Charge", type=Type.ELECTRIC, power=65, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        User recovers half the HP inflicted on opponent.
        """
        pass

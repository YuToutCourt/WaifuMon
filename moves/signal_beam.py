from .move import Move
from waifu_types.type import Type

class SignalBeam(Move):
    def __init__(self):
        super().__init__("Signal Beam", type=Type.BUG, power=75, accuracy=100, pp=15, proba_effect=10)

    def effect(self):
        """
        May confuse opponent.
        """
        pass

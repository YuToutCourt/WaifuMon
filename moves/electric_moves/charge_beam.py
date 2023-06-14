from ..move import Move
from waifu_types.type import Type

class ChargeBeam(Move):
    def __init__(self):
        super().__init__("Charge Beam", type=Type.ELECTRIC, power=50, accuracy=90, pp=10, priority=0, proba_effect=70)

    def effect(self):
        """
        May raise user's Special Attack.
        """
        pass

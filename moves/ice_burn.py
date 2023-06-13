from .move import Move
from waifu_types.type import Type

class IceBurn(Move):
    def __init__(self):
        super().__init__("Ice Burn", type=Type.ICE, power=140, accuracy=90, pp=5, proba_effect=30)

    def effect(self):
        """
        Charges on first turn, attacks on second. May burn opponent.
        """
        pass

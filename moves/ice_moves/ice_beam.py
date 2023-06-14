from ..move import Move
from waifu_types.type import Type

class IceBeam(Move):
    def __init__(self):
        super().__init__("Ice Beam", type=Type.ICE, power=90, accuracy=100, pp=10, priority=0, proba_effect=10)

    def effect(self):
        """
        May freeze opponent.
        """
        pass

from .move import Move
from waifu_types.type import Type

class TwinBeam(Move):
    def __init__(self):
        super().__init__("Twin Beam", type=Type.PSYCHIC, power=40, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Hits twice in one turn.
        """
        pass

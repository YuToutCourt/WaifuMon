from ..move import Move
from waifu_types.type import Type

class FrostBreath(Move):
    def __init__(self):
        super().__init__("Frost Breath", type=Type.ICE, power=60, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Always results in a critical hit.
        """
        pass

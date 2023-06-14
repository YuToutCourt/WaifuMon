from ..move import Move
from waifu_types.type import Type

class StormThrow(Move):
    def __init__(self):
        super().__init__("Storm Throw", type=Type.FIGHTING, power=60, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Always results in a critical hit.
        """
        pass

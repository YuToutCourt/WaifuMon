from ..move import Move
from waifu_types.type import Type

class Avalanche(Move):
    def __init__(self):
        super().__init__("Avalanche", type=Type.ICE, power=60, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Power doubles if user took damage first.
        """
        pass

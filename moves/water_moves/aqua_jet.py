from ..move import Move
from waifu_types.type import Type

class AquaJet(Move):
    def __init__(self):
        super().__init__("Aqua Jet", type=Type.WATER, power=40, accuracy=100, pp=20, priority=1, proba_effect=100)

    def effect(self):
        """
        User attacks first.
        """
        pass

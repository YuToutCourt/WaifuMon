from ..move import Move
from waifu_types.type import Type

class MaxLightning(Move):
    def __init__(self):
        super().__init__("Max Lightning", type=Type.ELECTRIC, power=0, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Electric type Dynamax move. Summons Electric Terrain.
        """
        pass

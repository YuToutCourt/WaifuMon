from ..move import Move
from waifu_types.type import Type

class WaterPledge(Move):
    def __init__(self):
        super().__init__("Water Pledge", type=Type.WATER, power=80, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Added effects appear if preceded by Fire Pledge or succeeded by Grass Pledge.
        """
        pass

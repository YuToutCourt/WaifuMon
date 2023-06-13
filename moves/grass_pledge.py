from .move import Move
from waifu_types.type import Type

class GrassPledge(Move):
    def __init__(self):
        super().__init__("Grass Pledge", type=Type.GRASS, power=80, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Added effects appear if preceded by Water Pledge or succeeded by Fire Pledge.
        """
        pass

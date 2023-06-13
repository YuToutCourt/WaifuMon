from .move import Move
from waifu_types.type import Type

class LeafTornado(Move):
    def __init__(self):
        super().__init__("Leaf Tornado", type=Type.GRASS, power=65, accuracy=90, pp=10, proba_effect=50)

    def effect(self):
        """
        May lower opponent's Accuracy.
        """
        pass

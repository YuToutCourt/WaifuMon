from ..move import Move
from waifu_types.type import Type

class Leafage(Move):
    def __init__(self):
        super().__init__("Leafage", type=Type.GRASS, power=40, accuracy=100, pp=40, priority=0, proba_effect=100)

    def effect(self):
        """
        Strikes opponent with leaves.
        """
        pass

from .move import Move
from waifu_types.type import Type

class CottonSpore(Move):
    def __init__(self):
        super().__init__("Cotton Spore", type=Type.GRASS, power=0, accuracy=100, pp=40, proba_effect=100)

    def effect(self):
        """
        Sharply lowers opponent's Speed.
        """
        pass

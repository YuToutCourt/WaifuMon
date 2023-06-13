from .move import Move
from waifu_types.type import Type

class Glaciate(Move):
    def __init__(self):
        super().__init__("Glaciate", type=Type.ICE, power=65, accuracy=95, pp=10, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Speed.
        """
        pass

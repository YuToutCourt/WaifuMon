from .move import Move
from waifu_types.type import Type

class Roost(Move):
    def __init__(self):
        super().__init__("Roost", type=Type.FLYING, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        User recovers half of its max HP and loses the Flying type temporarily.
        """
        pass

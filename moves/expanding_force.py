from .move import Move
from waifu_types.type import Type

class ExpandingForce(Move):
    def __init__(self):
        super().__init__("Expanding Force", type=Type.PSYCHIC, power=80, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Increases power and hits all opponents on Psychic Terrain.
        """
        pass

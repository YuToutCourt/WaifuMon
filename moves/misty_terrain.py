from .move import Move
from waifu_types.type import Type

class MistyTerrain(Move):
    def __init__(self):
        super().__init__("Misty Terrain", type=Type.FAIRY, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Protects the field from status conditions for 5 turns.
        """
        pass

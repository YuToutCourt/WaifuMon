from .move import Move
from waifu_types.type import Type

class SteelRoller(Move):
    def __init__(self):
        super().__init__("Steel Roller", type=Type.STEEL, power=130, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Fails if no Terrain in effect.
        """
        pass

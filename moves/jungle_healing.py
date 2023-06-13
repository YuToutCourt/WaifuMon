from .move import Move
from waifu_types.type import Type

class JungleHealing(Move):
    def __init__(self):
        super().__init__("Jungle Healing", type=Type.GRASS, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Restores team's HP and cures status conditions.
        """
        pass

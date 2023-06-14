from ..move import Move
from waifu_types.type import Type

class DynamaxCannon(Move):
    def __init__(self):
        super().__init__("Dynamax Cannon", type=Type.DRAGON, power=100, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Damage doubles if opponent is Dynamaxed.
        """
        pass

from .move import Move
from waifu_types.type import Type

class DragonRush(Move):
    def __init__(self):
        super().__init__("Dragon Rush", type=Type.DRAGON, power=100, accuracy=75, pp=10, proba_effect=20)

    def effect(self):
        """
        May cause flinching.
        """
        pass

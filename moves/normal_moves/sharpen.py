from ..move import Move
from waifu_types.type import Type

class Sharpen(Move):
    def __init__(self):
        super().__init__("Sharpen", type=Type.NORMAL, power=0, accuracy=100, pp=30, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises user's Attack.
        """
        pass

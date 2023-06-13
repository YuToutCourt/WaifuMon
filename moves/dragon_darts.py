from .move import Move
from waifu_types.type import Type

class DragonDarts(Move):
    def __init__(self):
        super().__init__("Dragon Darts", type=Type.DRAGON, power=50, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        User attacks twice.
        """
        pass

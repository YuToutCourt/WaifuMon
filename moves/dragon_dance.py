from .move import Move
from waifu_types.type import Type

class DragonDance(Move):
    def __init__(self):
        super().__init__("Dragon Dance", type=Type.DRAGON, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Raises user's Attack and Speed.
        """
        pass

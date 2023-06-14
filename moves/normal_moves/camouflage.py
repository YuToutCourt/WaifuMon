from ..move import Move
from waifu_types.type import Type

class Camouflage(Move):
    def __init__(self):
        super().__init__("Camouflage", type=Type.NORMAL, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Changes user's type according to the location.
        """
        pass

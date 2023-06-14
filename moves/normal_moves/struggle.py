from ..move import Move
from waifu_types.type import Type

class Struggle(Move):
    def __init__(self):
        super().__init__("Struggle", type=Type.NORMAL, power=50, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Only usable when all PP are gone. Hurts the user.
        """
        pass

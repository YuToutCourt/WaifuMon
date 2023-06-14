from ..move import Move
from waifu_types.type import Type

class TechnoBlast(Move):
    def __init__(self):
        super().__init__("Techno Blast", type=Type.NORMAL, power=120, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Type depends on the Drive being held.
        """
        pass

from ..move import Move
from waifu_types.type import Type

class PrismaticLaser(Move):
    def __init__(self):
        super().__init__("Prismatic Laser", type=Type.PSYCHIC, power=160, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        The user shoots powerful lasers using the power of a prism. The user can't move on the next turn.
        """
        pass

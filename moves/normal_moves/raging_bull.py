from ..move import Move
from waifu_types.type import Type

class RagingBull(Move):
    def __init__(self):
        super().__init__("Raging Bull", type=Type.NORMAL, power=90, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Type depends on the user’s form. Breaks through Reflect and Light Screen barriers.
        """
        pass

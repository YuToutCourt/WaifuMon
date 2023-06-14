from ..move import Move
from waifu_types.type import Type

class Yawn(Move):
    def __init__(self):
        super().__init__("Yawn", type=Type.NORMAL, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Puts opponent to sleep in the next turn.
        """
        pass

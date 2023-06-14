from ..move import Move
from waifu_types.type import Type

class Recycle(Move):
    def __init__(self):
        super().__init__("Recycle", type=Type.NORMAL, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        User's used hold item is restored.
        """
        pass

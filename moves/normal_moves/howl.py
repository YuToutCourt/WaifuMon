from ..move import Move
from waifu_types.type import Type

class Howl(Move):
    def __init__(self):
        super().__init__("Howl", type=Type.NORMAL, power=0, accuracy=100, pp=40, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises Attack of allies.
        """
        pass

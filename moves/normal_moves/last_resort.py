from ..move import Move
from waifu_types.type import Type

class LastResort(Move):
    def __init__(self):
        super().__init__("Last Resort", type=Type.NORMAL, power=140, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Can only be used after all other moves are used.
        """
        pass

from ..move import Move
from waifu_types.type import Type

class Attract(Move):
    def __init__(self):
        super().__init__("Attract", type=Type.NORMAL, power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        If opponent is the opposite gender, it's less likely to attack.
        """
        pass

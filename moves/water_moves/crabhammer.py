from ..move import Move
from waifu_types.type import Type

class Crabhammer(Move):
    def __init__(self):
        super().__init__("Crabhammer", type=Type.WATER, power=100, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio.
        """
        pass

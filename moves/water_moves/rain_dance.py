from ..move import Move
from waifu_types.type import Type

class RainDance(Move):
    def __init__(self):
        super().__init__("Rain Dance", type=Type.WATER, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Makes it rain for 5 turns.
        """
        pass

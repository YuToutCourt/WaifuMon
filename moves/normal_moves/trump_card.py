from ..move import Move
from waifu_types.type import Type

class TrumpCard(Move):
    def __init__(self):
        super().__init__("Trump Card", type=Type.NORMAL, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        The lower the PP, the higher the power.
        """
        pass

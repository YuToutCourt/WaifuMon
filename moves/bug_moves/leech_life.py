from ..move import Move
from waifu_types.type import Type

class LeechLife(Move):
    def __init__(self):
        super().__init__("Leech Life", type=Type.BUG, power=80, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        User recovers half the HP inflicted on opponent.
        """
        pass

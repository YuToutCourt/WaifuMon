from ..move import Move
from waifu_types.type import Type

class FutureSight(Move):
    def __init__(self):
        super().__init__("Future Sight", type=Type.PSYCHIC, power=120, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Damage occurs 2 turns later.
        """
        pass

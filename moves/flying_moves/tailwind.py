from ..move import Move
from waifu_types.type import Type

class Tailwind(Move):
    def __init__(self):
        super().__init__("Tailwind", type=Type.FLYING, power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Doubles Speed for 4 turns.
        """
        pass

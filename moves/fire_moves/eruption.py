from ..move import Move
from waifu_types.type import Type

class Eruption(Move):
    def __init__(self):
        super().__init__("Eruption", type=Type.FIRE, power=150, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Stronger when the user's HP is higher.
        """
        pass

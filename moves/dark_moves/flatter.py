from ..move import Move
from waifu_types.type import Type

class Flatter(Move):
    def __init__(self):
        super().__init__("Flatter", type=Type.DARK, power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Confuses opponent, but raises its Special Attack.
        """
        pass

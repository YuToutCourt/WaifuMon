from ..move import Move
from waifu_types.type import Type

class DynamicPunch(Move):
    def __init__(self):
        super().__init__("Dynamic Punch", type=Type.FIGHTING, power=100, accuracy=50, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Confuses opponent.
        """
        pass

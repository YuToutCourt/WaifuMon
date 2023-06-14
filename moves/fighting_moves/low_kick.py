from ..move import Move
from waifu_types.type import Type

class LowKick(Move):
    def __init__(self):
        super().__init__("Low Kick", type=Type.FIGHTING, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        The heavier the opponent, the stronger the attack.
        """
        pass

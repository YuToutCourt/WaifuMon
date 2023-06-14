from ..move import Move
from waifu_types.type import Type

class HeavySlam(Move):
    def __init__(self):
        super().__init__("Heavy Slam", type=Type.STEEL, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        The heavier the user, the stronger the attack.
        """
        pass

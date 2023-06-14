from ..move import Move
from waifu_types.type import Type

class DragonEnergy(Move):
    def __init__(self):
        super().__init__("Dragon Energy", type=Type.DRAGON, power=150, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        The higher the user's HP, the higher the power.
        """
        pass

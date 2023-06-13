from .move import Move
from waifu_types.type import Type

class DragonRage(Move):
    def __init__(self):
        super().__init__("Dragon Rage", type=Type.DRAGON, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Always inflicts 40 HP.
        """
        pass

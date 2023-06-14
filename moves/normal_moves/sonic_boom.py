from ..move import Move
from waifu_types.type import Type

class SonicBoom(Move):
    def __init__(self):
        super().__init__("Sonic Boom", type=Type.NORMAL, power=0, accuracy=90, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Always inflicts 20 HP.
        """
        pass

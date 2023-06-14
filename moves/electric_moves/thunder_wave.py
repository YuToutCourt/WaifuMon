from ..move import Move
from waifu_types.type import Type

class ThunderWave(Move):
    def __init__(self):
        super().__init__("Thunder Wave", type=Type.ELECTRIC, power=0, accuracy=90, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Paralyzes opponent.
        """
        pass

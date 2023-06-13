from .move import Move
from waifu_types.type import Type

class Ingrain(Move):
    def __init__(self):
        super().__init__("Ingrain", type=Type.GRASS, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        User restores HP each turn. User cannot escape/switch.
        """
        pass

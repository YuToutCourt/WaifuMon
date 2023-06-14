from ..move import Move
from waifu_types.type import Type

class NightDaze(Move):
    def __init__(self):
        super().__init__("Night Daze", type=Type.DARK, power=85, accuracy=95, pp=10, priority=0, proba_effect=40)

    def effect(self):
        """
        May lower opponent's Accuracy.
        """
        pass

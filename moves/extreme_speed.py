from .move import Move
from waifu_types.type import Type

class ExtremeSpeed(Move):
    def __init__(self):
        super().__init__("Extreme Speed", type=Type.NORMAL, power=80, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        User attacks first.
        """
        pass

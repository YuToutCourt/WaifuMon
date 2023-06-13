from .move import Move
from waifu_types.type import Type

class PowerTrick(Move):
    def __init__(self):
        super().__init__("Power Trick", type=Type.PSYCHIC, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        User's own Attack and Defense switch.
        """
        pass

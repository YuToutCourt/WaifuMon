from .move import Move
from waifu_types.type import Type

class AllySwitch(Move):
    def __init__(self):
        super().__init__("Ally Switch", type=Type.PSYCHIC, power=0, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        User switches with opposite teammate.
        """
        pass

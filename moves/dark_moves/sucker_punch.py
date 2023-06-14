from ..move import Move
from waifu_types.type import Type

class SuckerPunch(Move):
    def __init__(self):
        super().__init__("Sucker Punch", type=Type.DARK, power=70, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        User attacks first, but only works if opponent is readying an attack.
        """
        pass

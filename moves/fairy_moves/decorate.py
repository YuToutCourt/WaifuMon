from ..move import Move
from waifu_types.type import Type

class Decorate(Move):
    def __init__(self):
        super().__init__("Decorate", type=Type.FAIRY, power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply raises target's Attack and Special Attack.
        """
        pass

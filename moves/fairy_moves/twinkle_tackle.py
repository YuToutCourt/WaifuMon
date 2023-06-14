from ..move import Move
from waifu_types.type import Type

class TwinkleTackle(Move):
    def __init__(self):
        super().__init__("Twinkle Tackle", type=Type.FAIRY, power=0, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Fairy type Z-Move.
        """
        pass

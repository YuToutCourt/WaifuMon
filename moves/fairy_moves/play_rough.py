from ..move import Move
from waifu_types.type import Type

class PlayRough(Move):
    def __init__(self):
        super().__init__("Play Rough", type=Type.FAIRY, power=90, accuracy=90, pp=10, priority=0, proba_effect=10)

    def effect(self):
        """
        May lower opponent's Attack.
        """
        pass

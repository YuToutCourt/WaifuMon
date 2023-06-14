from ..move import Move
from waifu_types.type import Type

class Wake-UpSlap(Move):
    def __init__(self):
        super().__init__("Wake-Up Slap", type=Type.FIGHTING, power=70, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Power doubles if opponent is asleep, but wakes it up.
        """
        pass

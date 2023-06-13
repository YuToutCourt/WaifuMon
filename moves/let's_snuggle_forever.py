from .move import Move
from waifu_types.type import Type

class Let'sSnuggleForever(Move):
    def __init__(self):
        super().__init__("Let's Snuggle Forever", type=Type.FAIRY, power=190, accuracy=100, pp=1, proba_effect=100)

    def effect(self):
        """
        Mimikyu-exclusive Z-Move.
        """
        pass

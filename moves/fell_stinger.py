from .move import Move
from waifu_types.type import Type

class FellStinger(Move):
    def __init__(self):
        super().__init__("Fell Stinger", type=Type.BUG, power=50, accuracy=100, pp=25, proba_effect=100)

    def effect(self):
        """
        Drastically raises user's Attack if target is KO'd.
        """
        pass

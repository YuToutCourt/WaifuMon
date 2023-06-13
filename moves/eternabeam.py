from .move import Move
from waifu_types.type import Type

class Eternabeam(Move):
    def __init__(self):
        super().__init__("Eternabeam", type=Type.DRAGON, power=160, accuracy=90, pp=5, proba_effect=100)

    def effect(self):
        """
        User can't move on the next turn.
        """
        pass

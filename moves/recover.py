from .move import Move
from waifu_types.type import Type

class Recover(Move):
    def __init__(self):
        super().__init__("Recover", type=Type.NORMAL, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        User recovers half its max HP.
        """
        pass

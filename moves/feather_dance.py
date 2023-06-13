from .move import Move
from waifu_types.type import Type

class FeatherDance(Move):
    def __init__(self):
        super().__init__("Feather Dance", type=Type.FLYING, power=0, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Sharply lowers opponent's Attack.
        """
        pass

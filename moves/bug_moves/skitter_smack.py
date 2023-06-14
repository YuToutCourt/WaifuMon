from ..move import Move
from waifu_types.type import Type

class SkitterSmack(Move):
    def __init__(self):
        super().__init__("Skitter Smack", type=Type.BUG, power=70, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Sp. Attack.
        """
        pass

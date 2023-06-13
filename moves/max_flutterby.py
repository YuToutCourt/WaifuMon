from .move import Move
from waifu_types.type import Type

class MaxFlutterby(Move):
    def __init__(self):
        super().__init__("Max Flutterby", type=Type.BUG, power=0, accuracy=100, pp=—, proba_effect=100)

    def effect(self):
        """
        Bug type Dynamax move. Lowers the target's Special Attack.
        """
        pass

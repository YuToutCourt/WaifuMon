from .move import Move
from waifu_types.type import Type

class ScorchingSands(Move):
    def __init__(self):
        super().__init__("Scorching Sands", type=Type.GROUND, power=70, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        May burn the target.
        """
        pass

from ..move import Move
from waifu_types.type import Type

class ScaryFace(Move):
    def __init__(self):
        super().__init__("Scary Face", type=Type.NORMAL, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply lowers opponent's Speed.
        """
        pass

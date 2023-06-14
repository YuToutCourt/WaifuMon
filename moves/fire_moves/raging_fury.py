from ..move import Move
from waifu_types.type import Type

class RagingFury(Move):
    def __init__(self):
        super().__init__("Raging Fury", type=Type.FIRE, power=120, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        User keeps repeating the same move over and over.
        """
        pass

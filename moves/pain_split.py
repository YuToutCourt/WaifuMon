from .move import Move
from waifu_types.type import Type

class PainSplit(Move):
    def __init__(self):
        super().__init__("Pain Split", type=Type.NORMAL, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        The user's and opponent's HP becomes the average of both.
        """
        pass

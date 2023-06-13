from .move import Move
from waifu_types.type import Type

class Transform(Move):
    def __init__(self):
        super().__init__("Transform", type=Type.NORMAL, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        User takes on the form and attacks of the opponent.
        """
        pass

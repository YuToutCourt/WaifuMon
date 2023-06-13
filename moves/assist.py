from .move import Move
from waifu_types.type import Type

class Assist(Move):
    def __init__(self):
        super().__init__("Assist", type=Type.NORMAL, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        User performs a move known by its allies at random.
        """
        pass

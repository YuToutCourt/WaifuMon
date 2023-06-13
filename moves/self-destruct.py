from .move import Move
from waifu_types.type import Type

class Self-Destruct(Move):
    def __init__(self):
        super().__init__("Self-Destruct", type=Type.NORMAL, power=200, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        User faints.
        """
        pass

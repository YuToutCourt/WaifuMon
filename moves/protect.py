from .move import Move
from waifu_types.type import Type

class Protect(Move):
    def __init__(self):
        super().__init__("Protect", type=Type.NORMAL, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Protects the user, but may fail if used consecutively.
        """
        pass

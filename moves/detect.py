from .move import Move
from waifu_types.type import Type

class Detect(Move):
    def __init__(self):
        super().__init__("Detect", type=Type.FIGHTING, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Protects the user, but may fail if used consecutively.
        """
        pass

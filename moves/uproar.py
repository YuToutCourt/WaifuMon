from .move import Move
from waifu_types.type import Type

class Uproar(Move):
    def __init__(self):
        super().__init__("Uproar", type=Type.NORMAL, power=90, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        User attacks for 3 turns and prevents sleep.
        """
        pass

from .move import Move
from waifu_types.type import Type

class TripleAxel(Move):
    def __init__(self):
        super().__init__("Triple Axel", type=Type.ICE, power=20, accuracy=90, pp=10, proba_effect=100)

    def effect(self):
        """
        Attacks thrice with more power each time.
        """
        pass

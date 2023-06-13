from .move import Move
from waifu_types.type import Type

class IceBall(Move):
    def __init__(self):
        super().__init__("Ice Ball", type=Type.ICE, power=30, accuracy=90, pp=20, proba_effect=100)

    def effect(self):
        """
        Doubles in power each turn for 5 turns.
        """
        pass

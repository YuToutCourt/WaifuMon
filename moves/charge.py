from .move import Move
from waifu_types.type import Type

class Charge(Move):
    def __init__(self):
        super().__init__("Charge", type=Type.ELECTRIC, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Raises user's Special Defense and next Electric move's power increases.
        """
        pass

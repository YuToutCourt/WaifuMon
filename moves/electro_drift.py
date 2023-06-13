from .move import Move
from waifu_types.type import Type

class ElectroDrift(Move):
    def __init__(self):
        super().__init__("Electro Drift", type=Type.ELECTRIC, power=100, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Boosted even more if it's super-effective.
        """
        pass

from .move import Move
from waifu_types.type import Type

class PlasmaFists(Move):
    def __init__(self):
        super().__init__("Plasma Fists", type=Type.ELECTRIC, power=100, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Changes Normal-type moves to Electric-type moves.
        """
        pass

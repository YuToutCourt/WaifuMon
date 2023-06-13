from .move import Move
from waifu_types.type import Type

class MatBlock(Move):
    def __init__(self):
        super().__init__("Mat Block", type=Type.FIGHTING, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Protects teammates from damaging moves.
        """
        pass

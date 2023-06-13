from .move import Move
from waifu_types.type import Type

class Instruct(Move):
    def __init__(self):
        super().__init__("Instruct", type=Type.PSYCHIC, power=0, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Allows an ally to use a move instead.
        """
        pass

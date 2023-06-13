from .move import Move
from waifu_types.type import Type

class Outrage(Move):
    def __init__(self):
        super().__init__("Outrage", type=Type.DRAGON, power=120, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        User attacks for 2-3 turns but then becomes confused.
        """
        pass

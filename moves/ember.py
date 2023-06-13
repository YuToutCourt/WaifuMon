from .move import Move
from waifu_types.type import Type

class Ember(Move):
    def __init__(self):
        super().__init__("Ember", type=Type.FIRE, power=40, accuracy=100, pp=25, proba_effect=10)

    def effect(self):
        """
        May burn opponent.
        """
        pass

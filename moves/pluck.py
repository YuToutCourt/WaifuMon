from .move import Move
from waifu_types.type import Type

class Pluck(Move):
    def __init__(self):
        super().__init__("Pluck", type=Type.FLYING, power=60, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        If the opponent is holding a berry, its effect is stolen by user.
        """
        pass

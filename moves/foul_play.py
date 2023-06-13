from .move import Move
from waifu_types.type import Type

class FoulPlay(Move):
    def __init__(self):
        super().__init__("Foul Play", type=Type.DARK, power=95, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Uses the opponent's Attack stat.
        """
        pass

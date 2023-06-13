from .move import Move
from waifu_types.type import Type

class PsychUp(Move):
    def __init__(self):
        super().__init__("Psych Up", type=Type.NORMAL, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Copies the opponent's stat changes.
        """
        pass

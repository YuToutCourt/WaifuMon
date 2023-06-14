from ..move import Move
from waifu_types.type import Type

class Assurance(Move):
    def __init__(self):
        super().__init__("Assurance", type=Type.DARK, power=60, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Power doubles if opponent already took damage in the same turn.
        """
        pass

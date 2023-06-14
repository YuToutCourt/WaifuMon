from ..move import Move
from waifu_types.type import Type

class Sandstorm(Move):
    def __init__(self):
        super().__init__("Sandstorm", type=Type.ROCK, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Creates a sandstorm for 5 turns.
        """
        pass

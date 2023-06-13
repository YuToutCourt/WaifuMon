from .move import Move
from waifu_types.type import Type

class Metronome(Move):
    def __init__(self):
        super().__init__("Metronome", type=Type.NORMAL, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        User performs almost any move in the game at random.
        """
        pass

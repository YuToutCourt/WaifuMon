from .move import Move
from waifu_types.type import Type

class TarShot(Move):
    def __init__(self):
        super().__init__("Tar Shot", type=Type.ROCK, power=0, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Lowers the opponent's Speed and makes them weaker to Fire-type moves.
        """
        pass

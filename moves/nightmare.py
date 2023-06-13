from .move import Move
from waifu_types.type import Type

class Nightmare(Move):
    def __init__(self):
        super().__init__("Nightmare", type=Type.GHOST, power=0, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        The sleeping opponent loses 25% of its max HP each turn.
        """
        pass

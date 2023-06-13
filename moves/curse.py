from .move import Move
from waifu_types.type import Type

class Curse(Move):
    def __init__(self):
        super().__init__("Curse", type=Type.GHOST, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Ghosts lose 50% of max HP and curse the opponent; Non-Ghosts raise Attack, Defense and lower Speed.
        """
        pass

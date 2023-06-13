from .move import Move
from waifu_types.type import Type

class SkullBash(Move):
    def __init__(self):
        super().__init__("Skull Bash", type=Type.NORMAL, power=130, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Raises Defense on first turn, attacks on second.
        """
        pass

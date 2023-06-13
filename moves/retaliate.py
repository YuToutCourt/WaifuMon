from .move import Move
from waifu_types.type import Type

class Retaliate(Move):
    def __init__(self):
        super().__init__("Retaliate", type=Type.NORMAL, power=70, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Inflicts double damage if a teammate fainted on the last turn.
        """
        pass

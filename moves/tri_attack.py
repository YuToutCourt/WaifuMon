from .move import Move
from waifu_types.type import Type

class TriAttack(Move):
    def __init__(self):
        super().__init__("Tri Attack", type=Type.NORMAL, power=80, accuracy=100, pp=10, proba_effect=20)

    def effect(self):
        """
        May paralyze, burn or freeze opponent.
        """
        pass

from .move import Move
from waifu_types.type import Type

class DireClaw(Move):
    def __init__(self):
        super().__init__("Dire Claw", type=Type.POISON, power=80, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio. May poison, paralyze or make the opponent drowsy.
        """
        pass

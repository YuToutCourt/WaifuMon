from .move import Move
from waifu_types.type import Type

class All-OutPummeling(Move):
    def __init__(self):
        super().__init__("All-Out Pummeling", type=Type.FIGHTING, power=0, accuracy=100, pp=1, proba_effect=100)

    def effect(self):
        """
        Fighting type Z-Move.
        """
        pass

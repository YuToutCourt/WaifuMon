from .move import Move
from waifu_types.type import Type

class ToxicThread(Move):
    def __init__(self):
        super().__init__("Toxic Thread", type=Type.POISON, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Poisons opponent and lowers its Speed.
        """
        pass

from ..move import Move
from waifu_types.type import Type

class Incinerate(Move):
    def __init__(self):
        super().__init__("Incinerate", type=Type.FIRE, power=60, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Destroys the target's held berry.
        """
        pass

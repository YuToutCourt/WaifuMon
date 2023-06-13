from .move import Move
from waifu_types.type import Type

class VenomDrench(Move):
    def __init__(self):
        super().__init__("Venom Drench", type=Type.POISON, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Lowers poisoned opponent's Special Attack and Speed.
        """
        pass

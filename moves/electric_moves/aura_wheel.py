from ..move import Move
from waifu_types.type import Type

class AuraWheel(Move):
    def __init__(self):
        super().__init__("Aura Wheel", type=Type.ELECTRIC, power=110, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Changes type based on Morpeko's Mode.
        """
        pass

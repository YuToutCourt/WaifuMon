from .move import Move
from waifu_types.type import Type

class G-MaxWindRage(Move):
    def __init__(self):
        super().__init__("G-Max Wind Rage", type=Type.FLYING, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Corviknight-exclusive G-Max Move. Removes battlefield hazards.
        """
        pass

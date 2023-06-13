from .move import Move
from waifu_types.type import Type

class G-MaxStunShock(Move):
    def __init__(self):
        super().__init__("G-Max Stun Shock", type=Type.ELECTRIC, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Toxtricity-exclusive G-Max Move. Poisons or paralyzes opponents.
        """
        pass

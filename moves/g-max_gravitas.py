from .move import Move
from waifu_types.type import Type

class G-MaxGravitas(Move):
    def __init__(self):
        super().__init__("G-Max Gravitas", type=Type.PSYCHIC, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Orbeetle-exclusive G-Max Move. Summons Gravity for 5 turns.
        """
        pass

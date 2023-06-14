from ..move import Move
from waifu_types.type import Type

class LightScreen(Move):
    def __init__(self):
        super().__init__("Light Screen", type=Type.PSYCHIC, power=0, accuracy=100, pp=30, priority=0, proba_effect=100)

    def effect(self):
        """
        Halves damage from Special attacks for 5 turns.
        """
        pass

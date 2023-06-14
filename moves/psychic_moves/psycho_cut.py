from ..move import Move
from waifu_types.type import Type

class PsychoCut(Move):
    def __init__(self):
        super().__init__("Psycho Cut", type=Type.PSYCHIC, power=70, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio.
        """
        pass

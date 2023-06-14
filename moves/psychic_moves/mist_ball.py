from ..move import Move
from waifu_types.type import Type

class MistBall(Move):
    def __init__(self):
        super().__init__("Mist Ball", type=Type.PSYCHIC, power=70, accuracy=100, pp=5, priority=0, proba_effect=50)

    def effect(self):
        """
        May lower opponent's Special Attack.
        """
        pass
from ..move import Move
from waifu_types.type import Type

class RapidSpin(Move):
    def __init__(self):
        super().__init__("Rapid Spin", type=Type.NORMAL, power=50, accuracy=100, pp=40, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises user's Speed and removes entry hazards and trap move effects.
        """
        pass

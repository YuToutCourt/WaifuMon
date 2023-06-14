from ..move import Move
from waifu_types.type import Type

class Rollout(Move):
    def __init__(self):
        super().__init__("Rollout", type=Type.ROCK, power=30, accuracy=90, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Doubles in power each turn for 5 turns.
        """
        pass

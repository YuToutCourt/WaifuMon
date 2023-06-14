from ..move import Move
from waifu_types.type import Type

class SkyUppercut(Move):
    def __init__(self):
        super().__init__("Sky Uppercut", type=Type.FIGHTING, power=85, accuracy=90, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits the opponent, even during Fly.
        """
        pass

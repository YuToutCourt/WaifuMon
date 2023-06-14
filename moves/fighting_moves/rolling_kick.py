from ..move import Move
from waifu_types.type import Type

class RollingKick(Move):
    def __init__(self):
        super().__init__("Rolling Kick", type=Type.FIGHTING, power=60, accuracy=85, pp=15, priority=0, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass

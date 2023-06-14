from ..move import Move
from waifu_types.type import Type

class Present(Move):
    def __init__(self):
        super().__init__("Present", type=Type.NORMAL, power=0, accuracy=90, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Either deals damage or heals.
        """
        pass

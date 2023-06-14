from ..move import Move
from waifu_types.type import Type

class CeaselessEdge(Move):
    def __init__(self):
        super().__init__("Ceaseless Edge", type=Type.DARK, power=65, accuracy=90, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio. Damages target with splinters each turn.
        """
        pass

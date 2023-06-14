from ..move import Move
from waifu_types.type import Type

class FieryWrath(Move):
    def __init__(self):
        super().__init__("Fiery Wrath", type=Type.DARK, power=90, accuracy=100, pp=10, priority=0, proba_effect=20)

    def effect(self):
        """
        May cause flinching.
        """
        pass

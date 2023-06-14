from ..move import Move
from waifu_types.type import Type

class IronDefense(Move):
    def __init__(self):
        super().__init__("Iron Defense", type=Type.STEEL, power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply raises user's Defense.
        """
        pass

from ..move import Move
from waifu_types.type import Type

class ScaleShot(Move):
    def __init__(self):
        super().__init__("Scale Shot", type=Type.DRAGON, power=25, accuracy=90, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits 2-5 times in one turn. Boosts user's Speed but lowers its Defense.
        """
        pass

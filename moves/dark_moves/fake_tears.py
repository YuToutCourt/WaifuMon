from ..move import Move
from waifu_types.type import Type

class FakeTears(Move):
    def __init__(self):
        super().__init__("Fake Tears", type=Type.DARK, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply lowers opponent's Special Defense.
        """
        pass

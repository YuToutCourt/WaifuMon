from ..move import Move
from waifu_types.type import Type

class Dig(Move):
    def __init__(self):
        super().__init__("Dig", type=Type.GROUND, power=80, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Digs underground on first turn, attacks on second. Can also escape from caves.
        """
        pass

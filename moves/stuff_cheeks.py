from .move import Move
from waifu_types.type import Type

class StuffCheeks(Move):
    def __init__(self):
        super().__init__("Stuff Cheeks", type=Type.NORMAL, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        The user eats its held Berry, then sharply raises its Defense stat.
        """
        pass

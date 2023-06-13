from .move import Move
from waifu_types.type import Type

class MagnetRise(Move):
    def __init__(self):
        super().__init__("Magnet Rise", type=Type.ELECTRIC, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        User becomes immune to Ground-type moves for 5 turns.
        """
        pass

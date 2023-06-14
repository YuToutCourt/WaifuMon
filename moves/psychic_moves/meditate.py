from ..move import Move
from waifu_types.type import Type

class Meditate(Move):
    def __init__(self):
        super().__init__("Meditate", type=Type.PSYCHIC, power=0, accuracy=100, pp=40, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises user's Attack.
        """
        pass

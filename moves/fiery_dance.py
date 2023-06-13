from .move import Move
from waifu_types.type import Type

class FieryDance(Move):
    def __init__(self):
        super().__init__("Fiery Dance", type=Type.FIRE, power=80, accuracy=100, pp=10, proba_effect=50)

    def effect(self):
        """
        May raise user's Special Attack.
        """
        pass

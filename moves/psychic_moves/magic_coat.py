from ..move import Move
from waifu_types.type import Type

class MagicCoat(Move):
    def __init__(self):
        super().__init__("Magic Coat", type=Type.PSYCHIC, power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Reflects moves that cause status conditions back to the attacker.
        """
        pass

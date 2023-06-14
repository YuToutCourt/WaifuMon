from ..move import Move
from waifu_types.type import Type

class EerieSpell(Move):
    def __init__(self):
        super().__init__("Eerie Spell", type=Type.PSYCHIC, power=80, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Deals damage and reduces opponent's PP.
        """
        pass

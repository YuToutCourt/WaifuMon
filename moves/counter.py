from .move import Move
from waifu_types.type import Type

class Counter(Move):
    def __init__(self):
        super().__init__("Counter", type=Type.FIGHTING, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        When hit by a Physical Attack, user strikes back with 2x power.
        """
        pass

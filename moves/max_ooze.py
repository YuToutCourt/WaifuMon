from .move import Move
from waifu_types.type import Type

class MaxOoze(Move):
    def __init__(self):
        super().__init__("Max Ooze", type=Type.POISON, power=0, accuracy=100, pp=—, proba_effect=100)

    def effect(self):
        """
        Poison type Dynamax move. Increases the team's Special Attack.
        """
        pass

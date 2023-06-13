from .move import Move
from waifu_types.type import Type

class MaxKnuckle(Move):
    def __init__(self):
        super().__init__("Max Knuckle", type=Type.FIGHTING, power=0, accuracy=100, pp=—, proba_effect=100)

    def effect(self):
        """
        Fighting type Dynamax move. Increases the team's Attack.
        """
        pass

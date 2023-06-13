from .move import Move
from waifu_types.type import Type

class MaxAirstream(Move):
    def __init__(self):
        super().__init__("Max Airstream", type=Type.FLYING, power=0, accuracy=100, pp=—, proba_effect=100)

    def effect(self):
        """
        Flying type Dynamax move. Raises the team's Speed.
        """
        pass

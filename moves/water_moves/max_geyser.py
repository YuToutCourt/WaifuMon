from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MaxGeyser(Move):
    def __init__(self):
        super().__init__("Max Geyser", type=TypeFactory.create_type(Types.WATER), power=0, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Water type Dynamax move. Summons heavy rain.
        """
        pass

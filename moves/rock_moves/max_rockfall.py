from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MaxRockfall(Move):
    def __init__(self):
        super().__init__("Max Rockfall", type=TypeFactory.create_type(Types.ROCK), power=0, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Rock type Dynamax move. Summons a sandstorm.
        """
        pass

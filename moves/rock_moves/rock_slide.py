from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class RockSlide(Move):
    def __init__(self):
        super().__init__("Rock Slide", type=TypeFactory.create_type(Types.ROCK), power=75, accuracy=90, pp=10, priority=0, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass

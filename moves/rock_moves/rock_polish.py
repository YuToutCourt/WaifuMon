from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class RockPolish(Move):
    def __init__(self):
        super().__init__("Rock Polish", type=TypeFactory.create_type(Types.ROCK), power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply raises user's Speed.
        """
        pass

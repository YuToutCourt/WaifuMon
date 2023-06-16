from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Agility(Move):
    def __init__(self):
        super().__init__("Agility", type=TypeFactory.create_type(Types.PSYCHIC), power=0, accuracy=100, pp=30, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply raises user's Speed.
        """
        pass

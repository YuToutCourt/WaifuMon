from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class PsychoBoost(Move):
    def __init__(self):
        super().__init__("Psycho Boost", type=TypeFactory.create_type(Types.PSYCHIC), power=140, accuracy=90, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply lowers user's Special Attack.
        """
        pass

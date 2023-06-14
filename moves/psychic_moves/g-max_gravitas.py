from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxGravitas(Move):
    def __init__(self):
        super().__init__("G-Max Gravitas", type=TypeFactory.create_type(Types.PSYCHIC), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Orbeetle-exclusive G-Max Move. Summons Gravity for 5 turns.
        """
        pass

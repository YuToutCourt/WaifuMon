from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class StrengthSap(Move):
    def __init__(self):
        super().__init__("Strength Sap", type=TypeFactory.create_type(Types.GRASS), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        The user restores its HP by the same amount as the target's Attack stat. It also lowers the target's Attack stat.
        """
        pass

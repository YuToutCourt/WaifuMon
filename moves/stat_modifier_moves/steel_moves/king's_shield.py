from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class KingShield(Move):
    def __init__(self):
        super().__init__("King's Shield", type=TypeFactory.create_type(Types.STEEL), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Protects the user and lowers opponent's Attack on contact.
        """
        pass

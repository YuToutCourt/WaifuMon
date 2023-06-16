from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SilkTrap(Move):
    def __init__(self):
        super().__init__("Silk Trap", type=TypeFactory.create_type(Types.BUG), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Protects the user and lowers opponent's Speed on contact.
        """
        pass

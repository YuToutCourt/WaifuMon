from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class BaddyBad(Move):
    def __init__(self):
        super().__init__("Baddy Bad", type=TypeFactory.create_type(Types.DARK), power=90, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Reduces damage from Physical attacks.
        """
        pass

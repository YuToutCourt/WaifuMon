from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class FocusPunch(Move):
    def __init__(self):
        super().__init__("Focus Punch", type=TypeFactory.create_type(Types.FIGHTING), power=150, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        If the user is hit before attacking, it flinches instead.
        """
        pass

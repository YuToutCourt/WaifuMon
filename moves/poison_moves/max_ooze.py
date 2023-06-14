from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MaxOoze(Move):
    def __init__(self):
        super().__init__("Max Ooze", type=TypeFactory.create_type(Types.POISON), power=0, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Poison type Dynamax move. Increases the team's Special Attack.
        """
        pass

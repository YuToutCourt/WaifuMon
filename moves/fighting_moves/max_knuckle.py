from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MaxKnuckle(Move):
    def __init__(self):
        super().__init__("Max Knuckle", type=TypeFactory.create_type(Types.FIGHTING), power=0, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Fighting type Dynamax move. Increases the team's Attack.
        """
        pass

from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MaxSteelspike(Move):
    def __init__(self):
        super().__init__("Max Steelspike", type=TypeFactory.create_type(Types.STEEL), power=0, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Steel type Dynamax move. Raises the team's Defense.
        """
        pass

from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MaxDarkness(Move):
    def __init__(self):
        super().__init__("Max Darkness", type=TypeFactory.create_type(Types.DARK), power=0, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Dark type Dynamax move. Lowers the target's Special Defense.
        """
        pass

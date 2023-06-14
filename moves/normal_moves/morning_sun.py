from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MorningSun(Move):
    def __init__(self):
        super().__init__("Morning Sun", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        User recovers HP. Amount varies with the weather.
        """
        pass

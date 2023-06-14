from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class HighHorsepower(Move):
    def __init__(self):
        super().__init__("High Horsepower", type=TypeFactory.create_type(Types.GROUND), power=95, accuracy=95, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        The user fiercely attacks the target using its entire body.
        """
        pass

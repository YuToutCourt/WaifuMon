from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class RapidSpin(Move):
    def __init__(self):
        super().__init__("Rapid Spin", type=TypeFactory.create_type(Types.NORMAL), power=50, accuracy=100, pp=40, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises user's Speed and removes entry hazards and trap move effects.
        """
        pass

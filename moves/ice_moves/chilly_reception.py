from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class ChillyReception(Move):
    def __init__(self):
        super().__init__("Chilly Reception", type=TypeFactory.create_type(Types.ICE), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Switches out and summons a snowstorm lasting 5 turns.
        """
        pass

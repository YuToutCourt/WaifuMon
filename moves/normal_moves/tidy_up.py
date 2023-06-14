from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class TidyUp(Move):
    def __init__(self):
        super().__init__("Tidy Up", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Removes the effects of entry hazards and Substitute, and boosts user’s Attack and Speed.
        """
        pass

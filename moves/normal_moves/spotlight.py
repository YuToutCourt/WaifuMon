from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Spotlight(Move):
    def __init__(self):
        super().__init__("Spotlight", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        The user shines a spotlight on the target so that only the target will be attacked during the turn.
        """
        pass

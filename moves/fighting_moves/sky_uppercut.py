from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SkyUppercut(Move):
    def __init__(self):
        super().__init__("Sky Uppercut", type=TypeFactory.create_type(Types.FIGHTING), power=85, accuracy=90, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits the opponent, even during Fly.
        """
        pass

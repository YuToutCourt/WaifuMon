from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class FlareBlitz(Move):
    def __init__(self):
        super().__init__("Flare Blitz", type=TypeFactory.create_type(Types.FIRE), power=120, accuracy=100, pp=15, priority=0, proba_effect=10)

    def effect(self):
        """
        User receives recoil damage. May burn opponent.
        """
        pass

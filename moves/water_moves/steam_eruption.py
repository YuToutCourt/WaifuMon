from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SteamEruption(Move):
    def __init__(self):
        super().__init__("Steam Eruption", type=TypeFactory.create_type(Types.WATER), power=110, accuracy=95, pp=5, priority=0, proba_effect=30)

    def effect(self):
        """
        May burn opponent.
        """
        pass

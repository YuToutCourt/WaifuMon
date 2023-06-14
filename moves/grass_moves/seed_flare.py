from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SeedFlare(Move):
    def __init__(self):
        super().__init__("Seed Flare", type=TypeFactory.create_type(Types.GRASS), power=120, accuracy=85, pp=5, priority=0, proba_effect=40)

    def effect(self):
        """
        May lower opponent's Special Defense.
        """
        pass

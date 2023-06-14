from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class FlashCannon(Move):
    def __init__(self):
        super().__init__("Flash Cannon", type=TypeFactory.create_type(Types.STEEL), power=80, accuracy=100, pp=10, priority=0, proba_effect=10)

    def effect(self):
        """
        May lower opponent's Special Defense.
        """
        pass

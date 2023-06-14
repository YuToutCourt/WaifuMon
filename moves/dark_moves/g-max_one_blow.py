from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxOneBlow(Move):
    def __init__(self):
        super().__init__("G-Max One Blow", type=TypeFactory.create_type(Types.DARK), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Urshifu Single-Strike Style-exclusive G-Max Move. Strikes through Max Guard and Protect.
        """
        pass

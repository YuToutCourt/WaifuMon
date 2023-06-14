from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class IceBurn(Move):
    def __init__(self):
        super().__init__("Ice Burn", type=TypeFactory.create_type(Types.ICE), power=140, accuracy=90, pp=5, priority=0, proba_effect=30)

    def effect(self):
        """
        Charges on first turn, attacks on second. May burn opponent.
        """
        pass

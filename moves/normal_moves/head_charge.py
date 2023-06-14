from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class HeadCharge(Move):
    def __init__(self):
        super().__init__("Head Charge", type=TypeFactory.create_type(Types.NORMAL), power=120, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        User receives recoil damage.
        """
        pass

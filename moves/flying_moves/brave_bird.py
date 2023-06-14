from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class BraveBird(Move):
    def __init__(self):
        super().__init__("Brave Bird", type=TypeFactory.create_type(Types.FLYING), power=120, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        User receives recoil damage.
        """
        pass

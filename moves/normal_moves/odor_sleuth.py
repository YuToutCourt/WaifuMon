from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class OdorSleuth(Move):
    def __init__(self):
        super().__init__("Odor Sleuth", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=40, priority=0, proba_effect=100)

    def effect(self):
        """
        Resets opponent's Evasiveness, and allows Normal- and Fighting-type attacks to hit Ghosts.
        """
        pass

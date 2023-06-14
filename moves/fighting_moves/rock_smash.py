from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class RockSmash(Move):
    def __init__(self):
        super().__init__("Rock Smash", type=TypeFactory.create_type(Types.FIGHTING), power=40, accuracy=100, pp=15, priority=0, proba_effect=50)

    def effect(self):
        """
        May lower opponent's Defense.
        """
        pass

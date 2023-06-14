from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class ThunderWave(Move):
    def __init__(self):
        super().__init__("Thunder Wave", type=TypeFactory.create_type(Types.ELECTRIC), power=0, accuracy=90, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Paralyzes opponent.
        """
        pass

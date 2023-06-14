from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class GuardianofAlola(Move):
    def __init__(self):
        super().__init__("Guardian of Alola", type=TypeFactory.create_type(Types.FAIRY), power=0, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Tapu-exclusive Z-move. Cuts opponent's HP by 75%.
        """
        pass

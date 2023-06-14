from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxCuddle(Move):
    def __init__(self):
        super().__init__("G-Max Cuddle", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Eevee-exclusive G-Max Move. Infatuates opponents.
        """
        pass

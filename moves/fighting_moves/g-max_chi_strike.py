from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxChiStrike(Move):
    def __init__(self):
        super().__init__("G-Max Chi Strike", type=TypeFactory.create_type(Types.FIGHTING), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Machamp-exclusive G-Max Move. Increases critical hit ratio.
        """
        pass

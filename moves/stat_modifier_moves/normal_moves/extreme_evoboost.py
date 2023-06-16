from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class ExtremeEvoboost(Move):
    def __init__(self):
        super().__init__("Extreme Evoboost", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Eevee-exclusive Z-Move. Sharply raises all stats.
        """
        pass

from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class NastyPlot(Move):
    def __init__(self):
        super().__init__("Nasty Plot", type=TypeFactory.create_type(Types.DARK), power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply raises user's Special Attack.
        """
        pass

from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class PlasmaFists(Move):
    def __init__(self):
        super().__init__("Plasma Fists", type=TypeFactory.create_type(Types.ELECTRIC), power=100, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Changes Normal-type moves to Electric-type moves.
        """
        pass

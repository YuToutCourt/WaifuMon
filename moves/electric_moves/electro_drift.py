from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class ElectroDrift(Move):
    def __init__(self):
        super().__init__("Electro Drift", type=TypeFactory.create_type(Types.ELECTRIC), power=100, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Boosted even more if it's super-effective.
        """
        pass

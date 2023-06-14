from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class FieryDance(Move):
    def __init__(self):
        super().__init__("Fiery Dance", type=TypeFactory.create_type(Types.FIRE), power=80, accuracy=100, pp=10, priority=0, proba_effect=50)

    def effect(self):
        """
        May raise user's Special Attack.
        """
        pass

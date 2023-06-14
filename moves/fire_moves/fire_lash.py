from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class FireLash(Move):
    def __init__(self):
        super().__init__("Fire Lash", type=TypeFactory.create_type(Types.FIRE), power=80, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        The user strikes the target with a burning lash. This also lowers the target's Defense stat.
        """
        pass

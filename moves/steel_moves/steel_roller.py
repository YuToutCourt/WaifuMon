from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SteelRoller(Move):
    def __init__(self):
        super().__init__("Steel Roller", type=TypeFactory.create_type(Types.STEEL), power=130, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Fails if no Terrain in effect.
        """
        pass

from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class TearfulLook(Move):
    def __init__(self):
        super().__init__("Tearful Look", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        The user gets teary eyed to make the target lose its combative spirit. This lowers the target's Attack and Sp. Atk stats.
        """
        pass

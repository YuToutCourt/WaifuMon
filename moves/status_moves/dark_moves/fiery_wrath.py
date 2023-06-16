from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class FieryWrath(Move):
    def __init__(self):
        super().__init__("Fiery Wrath", type=TypeFactory.create_type(Types.DARK), power=90, accuracy=100, pp=10, priority=0, proba_effect=20)

    def effect(self):
        """
        May cause flinching.
        """
        pass

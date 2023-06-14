from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Dig(Move):
    def __init__(self):
        super().__init__("Dig", type=TypeFactory.create_type(Types.GROUND), power=80, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Digs underground on first turn, attacks on second. Can also escape from caves.
        """
        pass

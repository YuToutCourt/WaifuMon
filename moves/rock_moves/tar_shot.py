from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class TarShot(Move):
    def __init__(self):
        super().__init__("Tar Shot", type=TypeFactory.create_type(Types.ROCK), power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers the opponent's Speed and makes them weaker to Fire-type moves.
        """
        pass

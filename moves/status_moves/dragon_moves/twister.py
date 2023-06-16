from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Twister(Move):
    def __init__(self):
        super().__init__("Twister", type=TypeFactory.create_type(Types.DRAGON), power=40, accuracy=100, pp=20, priority=0, proba_effect=20)

    def effect(self):
        """
        May cause flinching. Hits Pok�mon using Fly/Bounce with double power.
        """
        pass

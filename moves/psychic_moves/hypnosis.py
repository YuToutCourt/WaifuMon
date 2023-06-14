from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Hypnosis(Move):
    def __init__(self):
        super().__init__("Hypnosis", type=TypeFactory.create_type(Types.PSYCHIC), power=0, accuracy=60, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Puts opponent to sleep.
        """
        pass

from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SleepPowder(Move):
    def __init__(self):
        super().__init__("Sleep Powder", type=TypeFactory.create_type(Types.GRASS), power=0, accuracy=75, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Puts opponent to sleep.
        """
        pass

from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class PulverizingPancake(Move):
    def __init__(self):
        super().__init__("Pulverizing Pancake", type=TypeFactory.create_type(Types.NORMAL), power=210, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Snorlax-exclusive Normal type Z-Move.
        """
        pass

from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class ToxicSpikes(Move):
    def __init__(self):
        super().__init__("Toxic Spikes", type=TypeFactory.create_type(Types.POISON), power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Poisons opponents when they switch into battle.
        """
        pass

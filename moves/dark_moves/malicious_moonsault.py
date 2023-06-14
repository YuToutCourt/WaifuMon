from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MaliciousMoonsault(Move):
    def __init__(self):
        super().__init__("Malicious Moonsault", type=TypeFactory.create_type(Types.DARK), power=180, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Incineroar-exclusive Z-Move.
        """
        pass

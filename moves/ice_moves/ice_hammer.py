from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class IceHammer(Move):
    def __init__(self):
        super().__init__("Ice Hammer", type=TypeFactory.create_type(Types.ICE), power=100, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        The user swings and hits with its strong, heavy fist. It lowers the user's Speed, however.
        """
        pass

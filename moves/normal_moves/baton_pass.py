from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class BatonPass(Move):
    def __init__(self):
        super().__init__("Baton Pass", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=40, priority=0, proba_effect=100)

    def effect(self):
        """
        User switches out and gives stat changes to the incoming Pokemon.
        """
        pass

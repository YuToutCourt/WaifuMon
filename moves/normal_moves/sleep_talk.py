from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SleepTalk(Move):
    def __init__(self):
        super().__init__("Sleep Talk", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        User performs one of its own moves while sleeping.
        """
        pass

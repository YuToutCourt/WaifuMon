from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class RevelationDance(Move):
    def __init__(self):
        super().__init__("Revelation Dance", type=TypeFactory.create_type(Types.NORMAL), power=90, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Type changes based on Oricorio's form.
        """
        pass

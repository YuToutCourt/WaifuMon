from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class NoxiousTorque(Move):
    def __init__(self):
        super().__init__("Noxious Torque", type=TypeFactory.create_type(Types.POISON), power=100, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass

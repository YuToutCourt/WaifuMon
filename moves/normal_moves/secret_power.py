from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SecretPower(Move):
    def __init__(self):
        super().__init__("Secret Power", type=TypeFactory.create_type(Types.NORMAL), power=70, accuracy=100, pp=20, priority=0, proba_effect=30)

    def effect(self):
        """
        Effects of the attack vary with the location.
        """
        pass

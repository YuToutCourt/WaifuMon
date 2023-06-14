from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SpikyShield(Move):
    def __init__(self):
        super().__init__("Spiky Shield", type=TypeFactory.create_type(Types.GRASS), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Protects the user and inflicts damage on contact.
        """
        pass

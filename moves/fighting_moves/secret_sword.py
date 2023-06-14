from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SecretSword(Move):
    def __init__(self):
        super().__init__("Secret Sword", type=TypeFactory.create_type(Types.FIGHTING), power=85, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Inflicts damage based on the target's Defense, not Special Defense.
        """
        pass

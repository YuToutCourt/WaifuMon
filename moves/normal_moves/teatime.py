from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Teatime(Move):
    def __init__(self):
        super().__init__("Teatime", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Forces all Pokémon on the field to eat their berries.
        """
        pass

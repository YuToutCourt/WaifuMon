from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class FlowerShield(Move):
    def __init__(self):
        super().__init__("Flower Shield", type=TypeFactory.create_type(Types.FAIRY), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply raises Defense of all Grass-type Pokémon on the field.
        """
        pass

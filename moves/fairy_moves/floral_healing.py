from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class FloralHealing(Move):
    def __init__(self):
        super().__init__("Floral Healing", type=TypeFactory.create_type(Types.FAIRY), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        The user restores the target's HP by up to half of its max HP. It restores more HP when the terrain is grass.
        """
        pass

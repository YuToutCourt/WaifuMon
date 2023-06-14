from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class GastroAcid(Move):
    def __init__(self):
        super().__init__("Gastro Acid", type=TypeFactory.create_type(Types.POISON), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Cancels out the effect of the opponent's Ability.
        """
        pass

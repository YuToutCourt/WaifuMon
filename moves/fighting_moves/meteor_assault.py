from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MeteorAssault(Move):
    def __init__(self):
        super().__init__("Meteor Assault", type=TypeFactory.create_type(Types.FIGHTING), power=150, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        User must recharge next turn.
        """
        pass

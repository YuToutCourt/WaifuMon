from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class MeteorBeam(Move):
    def __init__(self):
        super().__init__(
            "Meteor Beam",
            type=TypeFactory.create_type(Types.ROCK),
            power=120,
            accuracy=90,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User gathers space power and boosts its Sp. Atk stat, then attacks the target on the next turn.
        """
        pass

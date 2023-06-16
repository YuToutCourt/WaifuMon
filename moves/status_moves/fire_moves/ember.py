from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Ember(Move):
    def __init__(self):
        super().__init__(
            "Ember",
            type=TypeFactory.create_type(Types.FIRE),
            power=40,
            accuracy=100,
            pp=25,
            priority=0,
            proba_effect=10,
        )

    def effect(self):
        """
        May burn opponent.
        """
        pass

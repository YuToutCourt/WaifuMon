from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class SacredFire(Move):
    def __init__(self):
        super().__init__(
            "Sacred Fire",
            type=TypeFactory.create_type(Types.FIRE),
            power=100,
            accuracy=95,
            pp=5,
            priority=0,
            proba_effect=50,
        )

    def effect(self):
        """
        May burn opponent.
        """
        pass

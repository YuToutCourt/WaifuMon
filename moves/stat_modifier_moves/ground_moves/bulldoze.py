from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Bulldoze(Move):
    def __init__(self):
        super().__init__(
            "Bulldoze",
            type=TypeFactory.create_type(Types.GROUND),
            power=60,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Lowers opponent's Speed.
        """
        pass

from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class RockTomb(Move):
    def __init__(self):
        super().__init__(
            "Rock Tomb",
            type=TypeFactory.create_type(Types.ROCK),
            power=60,
            accuracy=95,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Lowers opponent's Speed.
        """
        pass

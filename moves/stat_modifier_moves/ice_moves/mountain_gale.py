from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class MountainGale(Move):
    def __init__(self):
        super().__init__(
            "Mountain Gale",
            type=TypeFactory.create_type(Types.ICE),
            power=100,
            accuracy=85,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Lowers user's Speed.
        """
        pass

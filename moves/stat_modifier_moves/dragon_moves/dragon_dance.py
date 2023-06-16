from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class DragonDance(Move):
    def __init__(self):
        super().__init__(
            "Dragon Dance",
            type=TypeFactory.create_type(Types.DRAGON),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Raises user's Attack and Speed.
        """
        pass
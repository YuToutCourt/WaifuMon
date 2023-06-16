from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Trailblaze(Move):
    def __init__(self):
        super().__init__(
            "Trailblaze",
            type=TypeFactory.create_type(Types.GRASS),
            power=50,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Raises user's Speed.
        """
        pass

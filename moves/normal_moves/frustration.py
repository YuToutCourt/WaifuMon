from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Frustration(Move):
    def __init__(self):
        super().__init__(
            "Frustration",
            type=TypeFactory.create_type(Types.NORMAL),
            power=80,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Power decreases with higher Friendship.
        """
        pass

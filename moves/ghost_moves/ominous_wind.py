from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class OminousWind(Move):
    def __init__(self):
        super().__init__(
            "Ominous Wind",
            type=TypeFactory.create_type(Types.GHOST),
            power=60,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=10,
        )

    def effect(self):
        """
        May raise all user's stats at once.
        """
        pass

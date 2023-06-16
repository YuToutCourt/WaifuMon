from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class SeismicToss(Move):
    def __init__(self):
        super().__init__(
            "Seismic Toss",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Inflicts damage equal to user's level.
        """
        pass

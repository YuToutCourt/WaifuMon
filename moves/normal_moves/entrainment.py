from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Entrainment(Move):
    def __init__(self):
        super().__init__(
            "Entrainment",
            type=TypeFactory.create_type(Types.NORMAL),
            power=90,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Makes target's ability same as user's.
        """
        pass

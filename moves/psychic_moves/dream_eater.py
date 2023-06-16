from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class DreamEater(Move):
    def __init__(self):
        super().__init__(
            "Dream Eater",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=100,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User recovers half the HP inflicted on a sleeping opponent.
        """
        pass

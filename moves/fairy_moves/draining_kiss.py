from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class DrainingKiss(Move):
    def __init__(self):
        super().__init__(
            "Draining Kiss",
            type=TypeFactory.create_type(Types.FAIRY),
            power=50,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User recovers most the HP inflicted on opponent.
        """
        pass

from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Boomburst(Move):
    def __init__(self):
        super().__init__(
            "Boomburst",
            type=TypeFactory.create_type(Types.NORMAL),
            power=140,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Hits all adjacent Pokemon.
        """
        pass

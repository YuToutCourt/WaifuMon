from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class NaturePower(Move):
    def __init__(self):
        super().__init__(
            "Nature Power",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Uses a certain move based on the current terrain.
        """
        pass

from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class ThroatChop(Move):
    def __init__(self):
        super().__init__(
            "Throat Chop",
            type=TypeFactory.create_type(Types.DARK),
            power=80,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Prevents use of sound moves for two turns.
        """
        pass

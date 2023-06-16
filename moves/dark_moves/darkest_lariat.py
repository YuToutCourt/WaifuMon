from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class DarkestLariat(Move):
    def __init__(self):
        super().__init__(
            "Darkest Lariat",
            type=TypeFactory.create_type(Types.DARK),
            power=85,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Ignores opponent's stat changes.
        """
        pass

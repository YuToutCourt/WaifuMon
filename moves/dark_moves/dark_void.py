from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class DarkVoid(Move):
    def __init__(self):
        super().__init__(
            "Dark Void",
            type=TypeFactory.create_type(Types.DARK),
            power=0,
            accuracy=50,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Puts all adjacent opponents to sleep.
        """
        pass

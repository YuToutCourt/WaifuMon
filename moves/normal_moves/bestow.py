from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Bestow(Move):
    def __init__(self):
        super().__init__(
            "Bestow",
            type=TypeFactory.create_type(Types.NORMAL),
            power=50,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Gives the user's held item to the target.
        """
        pass

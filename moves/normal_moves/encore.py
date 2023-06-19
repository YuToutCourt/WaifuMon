from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Encore(Move):
    def __init__(self):
        super().__init__(
            "Encore",
            type=TypeFactory.create_type(Types.NORMAL),
            power=110,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Forces opponent to keep using its last move for 3 turns.
        """
        pass

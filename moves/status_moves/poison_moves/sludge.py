from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Sludge(Move):
    def __init__(self):
        super().__init__(
            "Sludge",
            type=TypeFactory.create_type(Types.POISON),
            power=65,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=30,
        )

    def effect(self):
        """
        May poison opponent.
        """
        pass

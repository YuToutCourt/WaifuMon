from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class SludgeBomb(Move):
    def __init__(self):
        super().__init__(
            "Sludge Bomb",
            type=TypeFactory.create_type(Types.POISON),
            power=90,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=30,
        )

    def effect(self):
        """
        May poison opponent.
        """
        pass

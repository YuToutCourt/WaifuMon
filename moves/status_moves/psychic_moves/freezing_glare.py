from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class FreezingGlare(Move):
    def __init__(self):
        super().__init__(
            "Freezing Glare",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=90,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=10,
        )

    def effect(self):
        """
        May freeze opponent.
        """
        pass
from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Meditate(Move):
    def __init__(self):
        super().__init__(
            "Meditate",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=0,
            accuracy=100,
            pp=40,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Raises user's Attack.
        """
        pass

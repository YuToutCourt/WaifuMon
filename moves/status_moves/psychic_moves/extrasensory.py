from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Extrasensory(Move):
    def __init__(self):
        super().__init__(
            "Extrasensory",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=80,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=10,
        )

    def effect(self):
        """
        May cause flinching.
        """
        pass

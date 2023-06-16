from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class HeartStamp(Move):
    def __init__(self):
        super().__init__(
            "Heart Stamp",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=60,
            accuracy=100,
            pp=25,
            priority=0,
            proba_effect=30,
        )

    def effect(self):
        """
        May cause flinching.
        """
        pass

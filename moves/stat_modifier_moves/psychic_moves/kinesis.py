from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Kinesis(Move):
    def __init__(self):
        super().__init__(
            "Kinesis",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=0,
            accuracy=80,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Lowers opponent's Accuracy.
        """
        pass

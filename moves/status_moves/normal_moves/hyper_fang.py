from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class HyperFang(Move):
    def __init__(self):
        super().__init__(
            "Hyper Fang",
            type=TypeFactory.create_type(Types.NORMAL),
            power=80,
            accuracy=90,
            pp=15,
            priority=0,
            proba_effect=10,
        )

    def effect(self):
        """
        May cause flinching.
        """
        pass

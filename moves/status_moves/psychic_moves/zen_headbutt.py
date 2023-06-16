from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class ZenHeadbutt(Move):
    def __init__(self):
        super().__init__(
            "Zen Headbutt",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=80,
            accuracy=90,
            pp=15,
            priority=0,
            proba_effect=20,
        )

    def effect(self):
        """
        May cause flinching.
        """
        pass

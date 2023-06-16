from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class LeechSeed(Move):
    def __init__(self):
        super().__init__(
            "Leech Seed",
            type=TypeFactory.create_type(Types.GRASS),
            power=0,
            accuracy=90,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Drains HP from opponent each turn.
        """
        pass

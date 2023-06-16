from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class DoomDesire(Move):
    def __init__(self):
        super().__init__(
            "Doom Desire",
            type=TypeFactory.create_type(Types.STEEL),
            power=140,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Damage occurs 2 turns later.
        """
        pass

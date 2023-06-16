from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class BlackHoleEclipse(Move):
    def __init__(self):
        super().__init__(
            "Black Hole Eclipse",
            type=TypeFactory.create_type(Types.DARK),
            power=0,
            accuracy=100,
            pp=1,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Dark type Z-Move.
        """
        pass

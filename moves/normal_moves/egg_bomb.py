from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class EggBomb(Move):
    def __init__(self):
        super().__init__(
            "Egg Bomb",
            type=TypeFactory.create_type(Types.NORMAL),
            power=100,
            accuracy=75,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        No effect.
        """
        pass

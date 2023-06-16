from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class FlameBurst(Move):
    def __init__(self):
        super().__init__(
            "Flame Burst",
            type=TypeFactory.create_type(Types.FIRE),
            power=70,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        May also injure nearby Pokemon.
        """
        pass

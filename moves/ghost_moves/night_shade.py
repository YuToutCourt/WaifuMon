from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class NightShade(Move):
    def __init__(self):
        super().__init__(
            "Night Shade",
            type=TypeFactory.create_type(Types.GHOST),
            power=0,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Inflicts damage equal to user's level.
        """
        pass

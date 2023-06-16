from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class ReflectType(Move):
    def __init__(self):
        super().__init__(
            "Reflect Type",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User becomes the target's type.
        """
        pass

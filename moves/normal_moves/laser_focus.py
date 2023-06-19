from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class LaserFocus(Move):
    def __init__(self):
        super().__init__(
            "Laser Focus",
            type=TypeFactory.create_type(Types.NORMAL),
            power=50,
            accuracy=100,
            pp=30,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User's next attack is guaranteed to result in a critical hit.
        """
        pass

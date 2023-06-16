from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class LockOn(Move):
    def __init__(self):
        super().__init__(
            "Lock-On",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User's next attack is guaranteed to hit.
        """
        pass

from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Doodle(Move):
    def __init__(self):
        super().__init__(
            "Doodle",
            type=TypeFactory.create_type(Types.NORMAL),
            power=100,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Changes the abilities of the user and its teammates to that of the target.
        """
        pass

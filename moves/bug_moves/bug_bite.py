from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class BugBite(Move):
    def __init__(self):
        super().__init__(
            "Bug Bite",
            type=TypeFactory.create_type(Types.BUG),
            power=60,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Receives the effect from the opponent's held berry.
        """
        pass

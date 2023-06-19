from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class BeatUp(Move):
    def __init__(self):
        super().__init__(
            "Beat Up",
            type=TypeFactory.create_type(Types.DARK),
            power=80,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        No effect.
        """
        pass

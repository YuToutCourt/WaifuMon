from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Punishment(Move):
    def __init__(self):
        super().__init__(
            "Punishment",
            type=TypeFactory.create_type(Types.DARK),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Power increases when opponent's stats have been raised.
        """
        pass

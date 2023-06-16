from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class RainDance(Move):
    def __init__(self):
        super().__init__(
            "Rain Dance",
            type=TypeFactory.create_type(Types.WATER),
            power=0,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Makes it rain for 5 turns.
        """
        pass

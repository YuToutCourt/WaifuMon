from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class DynamicPunch(Move):
    def __init__(self):
        super().__init__(
            "Dynamic Punch",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=100,
            accuracy=50,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Confuses opponent.
        """
        pass

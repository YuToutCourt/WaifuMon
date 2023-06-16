from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class FlyingPress(Move):
    def __init__(self):
        super().__init__(
            "Flying Press",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=100,
            accuracy=95,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Deals Fighting and Flying type damage.
        """
        pass

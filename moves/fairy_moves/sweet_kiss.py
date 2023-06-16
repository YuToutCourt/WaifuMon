from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class SweetKiss(Move):
    def __init__(self):
        super().__init__(
            "Sweet Kiss",
            type=TypeFactory.create_type(Types.FAIRY),
            power=0,
            accuracy=75,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Confuses opponent.
        """
        pass

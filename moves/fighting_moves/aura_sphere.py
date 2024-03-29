from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class AuraSphere(Move):
    def __init__(self):
        super().__init__(
            "Aura Sphere",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=80,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Ignores Accuracy and Evasiveness.
        """
        pass

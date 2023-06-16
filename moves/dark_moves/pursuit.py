from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Pursuit(Move):
    def __init__(self):
        super().__init__(
            "Pursuit",
            type=TypeFactory.create_type(Types.DARK),
            power=40,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Double power if the opponent is switching out.
        """
        pass

from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class PoisonPowder(Move):
    def __init__(self):
        super().__init__(
            "Poison Powder",
            type=TypeFactory.create_type(Types.POISON),
            power=0,
            accuracy=75,
            pp=35,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Poisons opponent.
        """
        pass

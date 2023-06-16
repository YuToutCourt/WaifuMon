from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Confusion(Move):
    def __init__(self):
        super().__init__(
            "Confusion",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=50,
            accuracy=100,
            pp=25,
            priority=0,
            proba_effect=10,
        )

    def effect(self):
        """
        May confuse opponent.
        """
        pass

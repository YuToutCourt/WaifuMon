from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class SaltCure(Move):
    def __init__(self):
        super().__init__(
            "Salt Cure",
            type=TypeFactory.create_type(Types.ROCK),
            power=40,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Deals damage each turn; Steel and Water types are more affected.
        """
        pass

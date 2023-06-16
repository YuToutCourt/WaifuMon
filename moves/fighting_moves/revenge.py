from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Revenge(Move):
    def __init__(self):
        super().__init__(
            "Revenge",
            type=TypeFactory.create_type(Types.FIGHTING),
            power=60,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Power increases if user was hit first.
        """
        pass

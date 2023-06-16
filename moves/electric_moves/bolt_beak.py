from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class BoltBeak(Move):
    def __init__(self):
        super().__init__(
            "Bolt Beak",
            type=TypeFactory.create_type(Types.ELECTRIC),
            power=85,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        If the user attacks before the target, the power of this move is doubled.
        """
        pass

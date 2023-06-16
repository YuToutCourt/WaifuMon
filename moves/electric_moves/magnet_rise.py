from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class MagnetRise(Move):
    def __init__(self):
        super().__init__(
            "Magnet Rise",
            type=TypeFactory.create_type(Types.ELECTRIC),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User becomes immune to Ground-type moves for 5 turns.
        """
        pass

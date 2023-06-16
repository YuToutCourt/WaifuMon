from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Rototiller(Move):
    def __init__(self):
        super().__init__(
            "Rototiller",
            type=TypeFactory.create_type(Types.GROUND),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Raises Attack and Special Attack of Grass-types.
        """
        pass

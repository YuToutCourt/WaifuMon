from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Coil(Move):
    def __init__(self):
        super().__init__(
            "Coil",
            type=TypeFactory.create_type(Types.POISON),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Raises user's Attack, Defense and Accuracy.
        """
        pass

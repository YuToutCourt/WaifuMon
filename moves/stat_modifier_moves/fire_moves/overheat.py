from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Overheat(Move):
    def __init__(self):
        super().__init__(
            "Overheat",
            type=TypeFactory.create_type(Types.FIRE),
            power=130,
            accuracy=90,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Sharply lowers user's Special Attack.
        """
        pass

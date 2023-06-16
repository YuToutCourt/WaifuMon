from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class LeafStorm(Move):
    def __init__(self):
        super().__init__(
            "Leaf Storm",
            type=TypeFactory.create_type(Types.GRASS),
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

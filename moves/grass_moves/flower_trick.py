from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class FlowerTrick(Move):
    def __init__(self):
        super().__init__(
            "Flower Trick",
            type=TypeFactory.create_type(Types.GRASS),
            power=70,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Never misses; always results in a critical hit.
        """
        pass

from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class LeafBlade(Move):
    def __init__(self):
        super().__init__(
            "Leaf Blade",
            type=TypeFactory.create_type(Types.GRASS),
            power=90,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        High critical hit ratio.
        """
        pass

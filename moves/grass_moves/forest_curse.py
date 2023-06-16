from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class ForestCurse(Move):
    def __init__(self):
        super().__init__(
            "Forest's Curse",
            type=TypeFactory.create_type(Types.GRASS),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Adds Grass type to opponent.
        """
        pass

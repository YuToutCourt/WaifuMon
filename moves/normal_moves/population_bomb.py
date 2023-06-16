from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class PopulationBomb(Move):
    def __init__(self):
        super().__init__(
            "Population Bomb",
            type=TypeFactory.create_type(Types.NORMAL),
            power=20,
            accuracy=90,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Hits 1-10 times in a row.
        """
        pass

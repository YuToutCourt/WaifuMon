from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class WaterShuriken(Move):
    def __init__(self):
        super().__init__(
            "Water Shuriken",
            type=TypeFactory.create_type(Types.WATER),
            power=15,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Hits 2-5 times in one turn.
        """
        pass

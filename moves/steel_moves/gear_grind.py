from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class GearGrind(Move):
    def __init__(self):
        super().__init__(
            "Gear Grind",
            type=TypeFactory.create_type(Types.STEEL),
            power=50,
            accuracy=85,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Hits twice in one turn.
        """
        pass

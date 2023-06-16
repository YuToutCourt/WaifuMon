from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class HydroPump(Move):
    def __init__(self):
        super().__init__(
            "Hydro Pump",
            type=TypeFactory.create_type(Types.WATER),
            power=110,
            accuracy=80,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """ """
        pass

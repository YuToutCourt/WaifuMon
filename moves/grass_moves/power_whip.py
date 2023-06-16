from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class PowerWhip(Move):
    def __init__(self):
        super().__init__(
            "Power Whip",
            type=TypeFactory.create_type(Types.GRASS),
            power=120,
            accuracy=85,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """ """
        pass

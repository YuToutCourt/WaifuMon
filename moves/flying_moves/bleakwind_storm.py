from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class BleakwindStorm(Move):
    def __init__(self):
        super().__init__(
            "Bleakwind Storm",
            type=TypeFactory.create_type(Types.FLYING),
            power=100,
            accuracy=80,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        May cause frostbite.
        """
        pass

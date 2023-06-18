from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class EarthPower(Move):
    def __init__(self):
        super().__init__(
            "Earth Power",
            type=TypeFactory.create_type(Types.GROUND),
            power=100,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=10,
        )

    def effect(self):
        """
        No effect.
        """
        pass

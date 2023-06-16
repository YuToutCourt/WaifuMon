from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class DrillRun(Move):
    def __init__(self):
        super().__init__(
            "Drill Run",
            type=TypeFactory.create_type(Types.GROUND),
            power=80,
            accuracy=95,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        High critical hit ratio.
        """
        pass

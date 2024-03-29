from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class InfernoOverdrive(Move):
    def __init__(self):
        super().__init__(
            "Inferno Overdrive",
            type=TypeFactory.create_type(Types.FIRE),
            power=180,
            accuracy=100,
            pp=1,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Fire type Z-Move.
        """
        pass

from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class TectonicRage(Move):
    def __init__(self):
        super().__init__(
            "Tectonic Rage",
            type=TypeFactory.create_type(Types.GROUND),
            power=0,
            accuracy=100,
            pp=1,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Ground type Z-Move.
        """
        pass

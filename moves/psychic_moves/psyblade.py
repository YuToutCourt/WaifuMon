from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Psyblade(Move):
    def __init__(self):
        super().__init__(
            "Psyblade",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=80,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Power increases on Electric Terrain.
        """
        pass

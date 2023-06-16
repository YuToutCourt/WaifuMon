from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class ExpandingForce(Move):
    def __init__(self):
        super().__init__(
            "Expanding Force",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=80,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Increases power and hits all opponents on Psychic Terrain.
        """
        pass

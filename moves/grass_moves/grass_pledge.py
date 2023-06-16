from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class GrassPledge(Move):
    def __init__(self):
        super().__init__(
            "Grass Pledge",
            type=TypeFactory.create_type(Types.GRASS),
            power=80,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Added effects appear if preceded by Water Pledge or succeeded by Fire Pledge.
        """
        pass

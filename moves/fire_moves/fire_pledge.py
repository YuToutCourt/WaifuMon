from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class FirePledge(Move):
    def __init__(self):
        super().__init__(
            "Fire Pledge",
            type=TypeFactory.create_type(Types.FIRE),
            power=80,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Added effects appear if combined with Grass Pledge or Water Pledge.
        """
        pass

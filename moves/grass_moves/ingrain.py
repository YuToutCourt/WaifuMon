from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Ingrain(Move):
    def __init__(self):
        super().__init__(
            "Ingrain",
            type=TypeFactory.create_type(Types.GRASS),
            power=0,
            accuracy=100,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User restores HP each turn. User cannot escape/switch.
        """
        pass

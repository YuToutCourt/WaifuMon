from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class LightofRuin(Move):
    def __init__(self):
        super().__init__(
            "Light of Ruin",
            type=TypeFactory.create_type(Types.FAIRY),
            power=140,
            accuracy=90,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User receives recoil damage.
        """
        pass

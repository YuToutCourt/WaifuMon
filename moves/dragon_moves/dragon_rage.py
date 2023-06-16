from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class DragonRage(Move):
    def __init__(self):
        super().__init__(
            "Dragon Rage",
            type=TypeFactory.create_type(Types.DRAGON),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Always inflicts 40 HP.
        """
        pass

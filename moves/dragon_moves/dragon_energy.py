from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class DragonEnergy(Move):
    def __init__(self):
        super().__init__(
            "Dragon Energy",
            type=TypeFactory.create_type(Types.DRAGON),
            power=150,
            accuracy=100,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        The higher the user's HP, the higher the power.
        """
        pass

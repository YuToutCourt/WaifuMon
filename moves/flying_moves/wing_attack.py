from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class WingAttack(Move):
    def __init__(self):
        super().__init__(
            "Wing Attack",
            type=TypeFactory.create_type(Types.FLYING),
            power=60,
            accuracy=100,
            pp=35,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """ 
        No effect.
        """
        pass

from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class HornAttack(Move):
    def __init__(self):
        super().__init__(
            "Horn Attack",
            type=TypeFactory.create_type(Types.NORMAL),
            power=65,
            accuracy=100,
            pp=25,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """ """
        pass

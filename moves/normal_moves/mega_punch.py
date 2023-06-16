from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class MegaPunch(Move):
    def __init__(self):
        super().__init__(
            "Mega Punch",
            type=TypeFactory.create_type(Types.NORMAL),
            power=80,
            accuracy=85,
            pp=20,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """ """
        pass

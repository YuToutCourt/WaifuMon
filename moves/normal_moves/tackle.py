from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Tackle(Move):
    def __init__(self):
        super().__init__(
            "Tackle",
            type=TypeFactory.create_type(Types.NORMAL),
            power=40,
            accuracy=100,
            pp=35,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """ """
        pass

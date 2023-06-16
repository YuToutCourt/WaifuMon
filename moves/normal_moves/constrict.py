from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Constrict(Move):
    def __init__(self):
        super().__init__(
            "Constrict",
            type=TypeFactory.create_type(Types.NORMAL),
            power=10,
            accuracy=100,
            pp=35,
            priority=0,
            proba_effect=10,
        )

    def effect(self):
        """
        May lower opponent's Speed by one stage.
        """
        pass

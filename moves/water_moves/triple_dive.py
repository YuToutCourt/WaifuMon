from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class TripleDive(Move):
    def __init__(self):
        super().__init__(
            "Triple Dive",
            type=TypeFactory.create_type(Types.WATER),
            power=30,
            accuracy=95,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Hits 3 times in a row.
        """
        pass

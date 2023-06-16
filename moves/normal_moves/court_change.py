from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class CourtChange(Move):
    def __init__(self):
        super().__init__(
            "Court Change",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Swaps the effects on either side of the field.
        """
        pass

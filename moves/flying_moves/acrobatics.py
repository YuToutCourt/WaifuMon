from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Acrobatics(Move):
    def __init__(self):
        super().__init__(
            "Acrobatics",
            type=TypeFactory.create_type(Types.FLYING),
            power=55,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Stronger when the user does not have a held item.
        """
        pass

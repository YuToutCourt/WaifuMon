from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Feint(Move):
    def __init__(self):
        super().__init__(
            "Feint",
            type=TypeFactory.create_type(Types.NORMAL),
            power=30,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Only hits if opponent uses Protect or Detect in the same turn.
        """
        pass

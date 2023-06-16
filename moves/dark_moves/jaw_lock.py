from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class JawLock(Move):
    def __init__(self):
        super().__init__(
            "Jaw Lock",
            type=TypeFactory.create_type(Types.DARK),
            power=80,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Prevents user and opponent from switching out.
        """
        pass

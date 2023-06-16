from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class WorkUp(Move):
    def __init__(self):
        super().__init__(
            "Work Up",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=100,
            pp=30,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Raises user's Attack and Special Attack.
        """
        pass

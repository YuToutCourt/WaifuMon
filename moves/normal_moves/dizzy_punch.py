from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class DizzyPunch(Move):
    def __init__(self):
        super().__init__(
            "Dizzy Punch",
            type=TypeFactory.create_type(Types.NORMAL),
            power=70,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=20,
        )

    def effect(self):
        """
        May confuse opponent.
        """
        pass

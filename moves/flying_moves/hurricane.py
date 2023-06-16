from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class Hurricane(Move):
    def __init__(self):
        super().__init__(
            "Hurricane",
            type=TypeFactory.create_type(Types.FLYING),
            power=110,
            accuracy=70,
            pp=10,
            priority=0,
            proba_effect=30,
        )

    def effect(self):
        """
        May confuse opponent.
        """
        pass

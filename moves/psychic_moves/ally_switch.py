from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class AllySwitch(Move):
    def __init__(self):
        super().__init__(
            "Ally Switch",
            type=TypeFactory.create_type(Types.PSYCHIC),
            power=0,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        User switches with opposite teammate.
        """
        pass

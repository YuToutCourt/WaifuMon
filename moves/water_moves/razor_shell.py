from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class RazorShell(Move):
    def __init__(self):
        super().__init__(
            "Razor Shell",
            type=TypeFactory.create_type(Types.WATER),
            power=75,
            accuracy=95,
            pp=10,
            priority=0,
            proba_effect=50,
        )

    def effect(self):
        """
        May lower opponent's Defense.
        """
        pass

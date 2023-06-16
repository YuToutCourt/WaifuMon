from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class EchoedVoice(Move):
    def __init__(self):
        super().__init__(
            "Echoed Voice",
            type=TypeFactory.create_type(Types.NORMAL),
            power=40,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Power increases each turn.
        """
        pass

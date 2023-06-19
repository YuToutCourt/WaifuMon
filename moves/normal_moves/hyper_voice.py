from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class HyperVoice(Move):
    def __init__(self):
        super().__init__(
            "Hyper Voice",
            type=TypeFactory.create_type(Types.NORMAL),
            power=90,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        No effect.
        """
        pass

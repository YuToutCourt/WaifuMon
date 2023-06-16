from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class StompingTantrum(Move):
    def __init__(self):
        super().__init__(
            "Stomping Tantrum",
            type=TypeFactory.create_type(Types.GROUND),
            power=75,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Driven by frustration, the user attacks the target. If the user's previous move has failed, the power of this move doubles.
        """
        pass

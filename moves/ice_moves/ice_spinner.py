from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class IceSpinner(Move):
    def __init__(self):
        super().__init__(
            "Ice Spinner",
            type=TypeFactory.create_type(Types.ICE),
            power=80,
            accuracy=100,
            pp=15,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Removes effects of Terrain.
        """
        pass

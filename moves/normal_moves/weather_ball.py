from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types


class WeatherBall(Move):
    def __init__(self):
        super().__init__(
            "Weather Ball",
            type=TypeFactory.create_type(Types.NORMAL),
            power=50,
            accuracy=100,
            pp=10,
            priority=0,
            proba_effect=100,
        )

    def effect(self):
        """
        Move's power and type changes with the weather.
        """
        pass

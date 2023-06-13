from .move import Move
from waifu_types.type import Type

class WeatherBall(Move):
    def __init__(self):
        super().__init__("Weather Ball", type=Type.NORMAL, power=50, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Move's power and type changes with the weather.
        """
        pass

from ..move import Move
from waifu_types.type import Type

class PowerTrip(Move):
    def __init__(self):
        super().__init__("Power Trip", type=Type.DARK, power=20, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        The user boasts its strength and attacks the target. The more the user's stats are raised, the greater the move's power.
        """
        pass

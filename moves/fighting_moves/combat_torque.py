from ..move import Move
from waifu_types.type import Type

class CombatTorque(Move):
    def __init__(self):
        super().__init__("Combat Torque", type=Type.FIGHTING, power=100, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass

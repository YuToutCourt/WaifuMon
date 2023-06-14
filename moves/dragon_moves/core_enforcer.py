from ..move import Move
from waifu_types.type import Type

class CoreEnforcer(Move):
    def __init__(self):
        super().__init__("Core Enforcer", type=Type.DRAGON, power=100, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Suppresses the target's ability if the target has already moved.
        """
        pass

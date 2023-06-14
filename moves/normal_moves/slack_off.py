from ..move import Move
from waifu_types.type import Type

class SlackOff(Move):
    def __init__(self):
        super().__init__("Slack Off", type=Type.NORMAL, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        User recovers half its max HP.
        """
        pass

from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types
from utils.logger import log

class HornDrill(Move):
    def __init__(self):
        super().__init__(
            "Horn Drill",
            type=TypeFactory.create_type(Types.NORMAL),
            power=0,
            accuracy=30,
            pp=5,
            priority=0,
            proba_effect=100,
        )

    def effect(self, waifu_user, waifu_receiver):
        """
        One-Hit-KO, if it hits.
        """
        waifu_receiver.hp = 0
        log(self.name, "makes", waifu_receiver.name, "faint")

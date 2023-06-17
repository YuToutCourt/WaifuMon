from .status_enum import StatusE
from abc import ABC, abstractmethod


class Status(ABC):
    def __init__(self, status: StatusE, waifu):
        self.status = status
        self.waifu = waifu
        self.turns = 1
        

    @abstractmethod
    def apply_status(self):
        pass
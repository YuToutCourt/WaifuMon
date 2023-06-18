from .status_enum import StatusE
from abc import ABC, abstractmethod


class Status(ABC):
    def __init__(self, status: StatusE, waifu, after_attack:bool):
        self.status = status
        self.waifu = waifu
        self.turns = 1
        self.after_attack = after_attack
        

    @abstractmethod
    def apply_status(self):
        pass
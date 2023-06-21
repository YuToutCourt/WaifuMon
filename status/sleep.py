from .status import Status
from .status_enum import StatusE
from utils.logger import log
from random import randint
from moves.enum_moves import Moves

class Sleep(Status):
    def __init__(self, waifu, afer_attack:bool):
        super().__init__(StatusE.SLEEP, waifu, afer_attack)
        self.max_turn = randint(1, 3)

    def apply_status(self):
        """
        Sleep status effect.
        The sleep condition (SLP) causes a Pokémon to be unable to use moves, 
        except Snore and Sleep Talk
        Max turn == random(1, 3)
        :return: True if the pokemon is able to attack else False
        """
        if self.waifu.move_to_use.name in [Moves.SNORE, Moves.SLEEP_TALK]:
            self.turns += 1
            return True
        
        elif self.turns == self.max_turn :
            self.waifu.status = None
            self.turns = 0
            log("Sleep", f"{self.waifu.name} is awake now!")
            return True
    
        else :
            log("Sleep", f"{self.waifu.name} is sleeping!")
            self.turns += 1
            return False



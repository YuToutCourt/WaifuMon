from player_script.player import Player
from game_script.npc import NPC

class Fight:
    def __init__(self, player:Player, enemy:NPC):
        self.player = player
        self.enemy = enemy
        self.tour = 0
    
    def run(self):
        pass

    def player_turn(self):
        pass

    def enemy_turn(self):
        pass

    def end_fight(self):
        pass

    
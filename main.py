import pygame

from game_script.game import Game

if __name__ == '__main__':

    # Initialisation de pygame
    pygame.init()
    game = Game().run()
import pygame

from character.player import Player
from utils.coordinates import Coordinates
from map.map_manager import MapManager


class Game:
    def __init__(self):
        screens = pygame.display.list_modes()

        # Choix de l'écran le plus grand
        largest_screen = max(screens, key=lambda s: s[0] * s[1])
        screen_width, screen_height = largest_screen

        self.screen = pygame.display.set_mode(
            (screen_width, screen_height), pygame.FULLSCREEN
        )

        pygame.display.set_caption("WaifuMon")

        coordinates = Coordinates(0, 0)
        self.player = Player(coordinates)
        self.map_manager = MapManager(self.screen, self.player)

        self.map_manager.get_map().load_npc()

    def handle_input(self):
        """
        Gère les entrées clavier du joueur
        :return: True si le joueur a appuyé sur la touche SHIFT, False sinon
        """
        pressed = pygame.key.get_pressed()
        # if the player press the shift key
        if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]:
            # the player is running
            return self.player.move(pressed, True)

        return self.player.move(pressed, False)

    def run(self):
        """
        Boucle principale du jeu
        """
        running = True
        while running:
            current_map = self.map_manager.get_map()
            self.handle_input()
            current_map.move_npc()
            self.map_manager.update()
            self.map_manager.draw()
            current_map.handle_collisions()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
        pygame.quit()

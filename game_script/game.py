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

        pygame.display.set_caption("WaifuMon") # Titre de la fenêtre

        coordinates = Coordinates(0, 0) # Coordonnées du joueur
        self.player = Player(coordinates) # Création du joueur
        self.map_manager = MapManager(self.screen, self.player) # Création du gestionnaire de carte

        self.map_manager.get_map().load_npc() # Chargement des PNJ de la carte

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
            current_map = self.map_manager.get_map() # Récupération de la carte actuelle
            self.handle_input() # Gestion des entrées clavier
            current_map.move_npc() # Déplacement des PNJ
            self.map_manager.update() # Mise à jour de la carte
            self.map_manager.draw() # Affichage de la carte
            current_map.handle_collisions() # Gestion des collisions
            pygame.display.flip() # Mise à jour de l'écran

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    running = False
            
        pygame.quit() 

import pygame

from character.player import Player
from utils.coordinates import Coordinates
from map.map_manager import MapManager


class Game:
    def __init__(self):

        screen_width, screen_height = 1920, 1080 # Set the screen size

        self.screen = pygame.display.set_mode(
            (screen_width, screen_height), pygame.FULLSCREEN 
        )

        pygame.display.set_caption("WaifuMon")

        coordinates = Coordinates(0, 0) 
        self.player = Player(coordinates)
        self.map_manager = MapManager(self.screen, self.player) # Create the map manager

        self.map_manager.get_map().load_npc() 

    def handle_input(self):
        """
        Handle the input of the player
        :return: True if the player is running, False otherwise
        """
        pressed = pygame.key.get_pressed()
        # if the player press the shift key
        if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]:
            # the player is running
            return self.player.move(pressed, True) 

        return self.player.move(pressed, False) 

    def run(self):
        """
        Main loop of the game
        """
        running = True
        while running:
            current_map = self.map_manager.get_map() # Get the current map
            self.handle_input() # Handle the input of the player
            current_map.move_npc() # Move the npc
            self.map_manager.update() # Update the map
            self.map_manager.draw() # Draw the map 
            current_map.handle_collisions() # Handle the collisions for the current map
            pygame.display.flip() # Update the screen

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    running = False
            
        pygame.quit() 

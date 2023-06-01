import pygame

from utils.coordinates import Coordinates

class NPC(pygame.sprite.Sprite):
    def __init__(self, name, coordinates:Coordinates, dialog: str):
        super().__init__()
        self.name = name
        self.position = (coordinates.x, coordinates.y)
        self.dialog = dialog
        self.image = pygame.image.load("asset/Tileset/Characters/" + self.name + ".png")
        self.image = self.get_image(0, 0)
        self.image.set_colorkey((255, 0, 220))
        self.rect = self.image.get_rect()

    def handle_interaction(self):
        print(self.dialog)
        pygame.init()
        combat_screen = pygame.display.set_mode((800, 600))

        combat_running = True
        while combat_running:
            # Gérez les entrées utilisateur et les événements de Pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # L'utilisateur a demandé à quitter la fenêtre de combat
                    combat_running = False

            # Dessinez les images de combat et mettez-les à jour sur l'écran
            # combat_window.blit(background_image, (0, 0))
            # Dessinez les sprites de combat, etc.

            pygame.display.flip()

        pygame.quit()



    def update(self):
        self.rect.topleft = self.position

    def get_image(self, x:int, y:int):
        """
        Récupère une image dans le spritesheet
        
        :param x: position x de l'image dans le spritesheet
        :param y: position y de l'image dans le spritesheet

        :return: l'image récupérée
        """
        image = pygame.Surface([38, 46])
        image.blit(self.image, (0, 0), (x, y, 38, 46))

        return image
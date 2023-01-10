import pygame

# Initialisation de pygame
pygame.init()

# récupération des informations sur tous les écrans connectés
screens = pygame.display.list_modes()
screen_info = pygame.display.Info()

# Choix de l'écran le plus grand
largest_screen = max(screens, key=lambda s: s[0] * s[1])
screen_width, screen_height = largest_screen

# Création de la fenêtre
screen = pygame.display.set_mode((screen_width, screen_height),pygame.FULLSCREEN)

pygame.display.set_caption("WaifuMon")

# Boucle principale pour afficher la fenêtre
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

# Termination de pygame
pygame.quit()



import pygame
import random
import threading

from game_script.fight import Fight
from utils.logger import log


class FightScreen:
    def __init__(self, screen):
        pygame.init()
        pygame.display.set_caption("fight")
        self.screen = screen
        self.background = None
        self.waifu_front = None
        self.waifu_back = None
        self.figth = None

    def run_fight(self, player, npc):
        """
        Launch the fight
        """
        self.fight = Fight(player, npc)
        self.__fill_screen()
        self.__load_background()
        
        pygame.mixer.music.stop()
        pygame.mixer.music.load("asset/music/fight_theme.mp3")
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(-1)

        fight_thread = threading.Thread(target=self.fight.start)
        fight_thread.start()

        # Display the fight
        while self.fight.finished is False:
            event = pygame.event.get()
            self.__load_waifu(player, npc)
            self.__update_display(player, npc, event)

    def __fill_screen(self):
        """
        Fill the screen with black
        """
        COLOR = (0, 0, 0) # Black
        width = self.screen.get_width()
        height = self.screen.get_height()

        cubes = []
        cubes_size = min(width, height) // 10

        # TODO: On pourrait s'amuser à faire des animations différentes :D
        for x in range(0, self.screen.get_width(), cubes_size):
            for y in range(0, self.screen.get_height(), cubes_size): 
                cube = pygame.Rect(x, y, cubes_size, cubes_size)
                cubes.append(cube) 

        if random.randint(0, 1): # Randomly reverse the list of cubes to reverse the direction of the animation
            cubes = cubes[::-1] 

        for cube in cubes: 
            pygame.draw.rect(self.screen, COLOR, cube) # Draw the cube on the screen
            pygame.display.flip() 
            pygame.time.wait(5)

    def __load_background(self):
        """
        Load the background
        """
        background = pygame.image.load("asset/Battle/battleground2.jpg")

        self.background = pygame.transform.scale( # Resize the background to fit the screen
            background, (self.screen.get_width(), self.screen.get_height())
        )

    def __load_waifu(self, player, npc):
        """
        Load the waifu of the player and the npc
        """

        waifu_ = npc.get_waifu_in_fight()
        waifu__ = player.get_waifu_in_fight() 

        if waifu_ is not None: # If the npc has a waifu
            self.waifu_front = pygame.transform.scale( # Resize the waifu to fit the screen
                waifu_.get_front_image(),
                (self.screen.get_width() // 5, self.screen.get_height() // 3),
            )

        if waifu__ is not None: # If the player has a waifu
            self.waifu_back = pygame.transform.scale( # Resize the waifu to fit the screen
                waifu__.get_back_image(), 
                (self.screen.get_width() // 3.75, self.screen.get_height() // 1.75), 
            )

    def create_text(self, text, font_size, color, font=None):
        """
        Create a text
        """
        if font is None:
            font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, color)
        return text_surface

    def create_hp_bar(self, current_hp, max_hp, bar_width, bar_height):
            """
            Create an HP bar surface with a gradual color transition.
            """
            bar_surface = pygame.Surface((bar_width, bar_height))
            bar_surface.fill((255, 255, 255))  # Fill with white color

            # Calculate the width of the green portion of the bar
            green_width = int((current_hp / max_hp) * bar_width)

            # Calculate the RGB color based on HP percentage
            red = int((1 - current_hp / max_hp) * 255)
            green = int((current_hp / max_hp) * 255)
            color = (red, green, 60)
            
            # Draw the green portion of the bar
            green_rect = pygame.Rect(0, 0, green_width, bar_height)

            # If the hp if negative the color will not be generated and an error will be raised
            try:
                pygame.draw.rect(bar_surface, color, green_rect)
            except Exception as e:
                log("Color for hp bar", color, e)

            return bar_surface
    
    def create_pokeball(self, width, height, path):
        """
        Create a pokeball surface.
        """
        pokeball = pygame.image.load(f"asset/Battle/{path}") 
        pokeball = pygame.transform.scale(pokeball, (width, height)) # Resize the pokeball to fit the screen
        
        return pokeball


    def create_badge_status(self, width, height, path):
        """
        Create a badge status surface.
        """
        badge = pygame.image.load(f"asset/Battle/{path}")
        badge = pygame.transform.scale(badge, (width, height)) # Resize the badge to fit the screen
        
        return badge
    
    def draw_pokeballs(self, waifu_team, x_offset, y_offset, screen_width, screen_height):
        pokeballs = []
        for waifu in waifu_team:
            if waifu.KO:
                pokeballs.append(self.create_pokeball(52, 55, "icon_ball_faint.png"))
            elif waifu.status is not None:
                pokeballs.append(self.create_pokeball(52, 55, "icon_ball_status.png"))  # TODO: make a custom status pokeball for each status
            else:
                pokeballs.append(self.create_pokeball(52, 55, "icon_ball.png"))

        decalage = 0  # Offset for the pokeballs
        for pokeball in pokeballs:
            self.screen.blit(pokeball, (screen_width * x_offset + decalage, screen_height * y_offset))
            decalage += 55  # Increase the offset


    def __update_display(self, player_waifu, npc_waifu, event): 
        self.screen.blit(self.background, (0, 0) ) # Draw the background on the screen
        screen_width = self.screen.get_width()  # Get the width of the screen
        screen_height = self.screen.get_height() # Get the height of the screen

        self.draw_pokeballs(player_waifu.team, 0.760, 0.9371, screen_width, screen_height) # Draw the pokeballs of the player
        self.draw_pokeballs(npc_waifu.team, 0.0261, 0.146, screen_width, screen_height) # Draw the pokeballs of the npc

        # Position and dimensions calculations based on screen size
        player_name_x = int(screen_width * 0.760)
        player_name_y = int(screen_height * 0.8195)
        player_level_x = int(screen_width * 0.8855)
        player_level_y = int(screen_height * 0.8195)
        player_hp_x = int(screen_width * 0.8855)
        player_hp_y = int(screen_height * 0.87963)
        player_hp_bar_x = int(screen_width * 0.86355)
        player_hp_bar_y = int(screen_height * 0.85)

        npc_name_x = int(screen_width * 0.0261)
        npc_name_y = int(screen_height * 0.0352)
        npc_level_x = int(screen_width * 0.1563)
        npc_level_y = int(screen_height * 0.0352)
        npc_hp_x = int(screen_width * 0.08073)
        npc_hp_y = int(screen_height * 0.09445)
        npc_hp_bar_x = int(screen_width * 0.0292)
        npc_hp_bar_y = int(screen_height * 0.0667)

        waifu_player = player_waifu.get_waifu_in_fight()
        waifu_npc = npc_waifu.get_waifu_in_fight() 


        if waifu_player is not None: 

            if waifu_player.status is not None: 
                status_surface = self.create_badge_status(40, 40, f"{waifu_player.status.status.name}.png")
                self.screen.blit(status_surface, (screen_width * 0.78334, screen_height * 0.854)) # Draw the status badge on the screen


            waifu_player_name = waifu_player.name
            waifu_player_hp = waifu_player.hp
            waifu_player_max_hp = waifu_player.hp_max
            waifu_player_level = waifu_player.level

            player_name_surface = self.create_text(waifu_player_name, 30, (0, 0, 0)) # Create the text for the name of the waifu
            player_hp_surface = self.create_text(f"{round(waifu_player_hp)}/{waifu_player_max_hp}", 30, (0, 0, 0)) # Create the text for the HP of the waifu
            player_level_surface = self.create_text(f"Lv{waifu_player_level}", 30, (0, 0, 0))  # Create the text for the level of the waifu
            
            player_hp_bar = self.create_hp_bar(waifu_player_hp, waifu_player_max_hp, int(screen_width * 0.1063), int(screen_height * 0.013)) # Create an HP bar
            self.screen.blit(player_hp_bar, (player_hp_bar_x, player_hp_bar_y)) # Draw the HP bar on the screen

            self.screen.blit(player_name_surface, (player_name_x, player_name_y)) # Draw the name of the waifu on the screen
            self.screen.blit(player_level_surface, (player_level_x, player_level_y)) # Draw the level of the waifu on the screen
            self.screen.blit(player_hp_surface, (player_hp_x, player_hp_y)) # Draw the HP of the waifu on the screen

            self.screen.blit( # Draw the player's waifu on the screen
                self.waifu_back, 
                (self.screen.get_width() // 8, self.screen.get_height() // 2.2), # Position of the waifu on the screen
            )

        if waifu_npc is not None: 

            if waifu_npc.status is not None: # If the waifu of the npc has a status
                status_surface = self.create_badge_status(40, 40, f"{waifu_npc.status.status.name}.png") # Create a status badge
                self.screen.blit(status_surface, (screen_width * 0.2, screen_height * 0.075)) # Draw the status badge on the screen
        
            waifu_npc_name = waifu_npc.name
            waifu_npc_hp = waifu_npc.hp
            waifu_npc_max_hp = waifu_npc.hp_max
            waifu_npc_level = waifu_npc.level

            npc_hp_bar = self.create_hp_bar(waifu_npc_hp, waifu_npc_max_hp, int(screen_width * 0.1063), int(screen_height * 0.013)) # Create an HP bar
            self.screen.blit(npc_hp_bar, (npc_hp_bar_x, npc_hp_bar_y)) # Draw the HP bar on the screen

            npc_name_surface = self.create_text(waifu_npc_name, 30, (0, 0, 0)) # Create the text for the name of the waifu
            npc_hp_surface = self.create_text(f"{round(waifu_npc_hp)}/{waifu_npc_max_hp}", 30, (0, 0, 0)) # Create the text for the HP of the waifu
            npc_level_surface = self.create_text(f"Lv{waifu_npc_level}", 30, (0, 0, 0)) # Create the text for the level of the waifu

            self.screen.blit(npc_name_surface, (npc_name_x, npc_name_y)) # Draw the name of the waifu on the screen
            self.screen.blit(npc_level_surface, (npc_level_x, npc_level_y)) # Draw the level of the waifu on the screen
            self.screen.blit(npc_hp_surface, (npc_hp_x, npc_hp_y)) # Draw the HP of the waifu on the screen
       
            self.screen.blit( # Draw the npc's waifu on the screen
                self.waifu_front,
                (self.screen.get_width() // 1.5, self.screen.get_height() * 0.42), # Position of the waifu on the screen
            )


        pygame.display.flip() # Update the screen


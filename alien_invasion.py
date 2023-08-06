import sys
import pygame
from spaceship import Ship
from settings import Settings

class AlienInvasion:

    def __init__(self):
        #initialize the game
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # self.screen = pygame.display.set_mode((0, 0) , pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        


        pygame.display.set_caption("Alien Invasion")

        #bg color
        self.bg_color = self.settings.bg_color

        #bg image
        #load and resize
        self.bg_image = pygame.image.load('images/blacky.png')
        self.bg_image = pygame.transform.scale(self.bg_image, (self.settings.screen_width, self.settings.screen_height))  
        self.ship = Ship(self)

    def run_game(self):
        #start the main loop of the game
        while True:
            #keyboard and mouse events
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):        
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                 sys.exit()

    def _check_keyup_events(self, event):        
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False   
            elif event.key == pygame.K_q:
                 sys.exit()            

    def _update_screen(self):
            #redraw screen color
            self.screen.fill(self.bg_color)          
            #redraw screen color bg
            self.screen.blit(self.bg_image, (0, 0))
            self.ship.blitme()
            #most recent screen visibility
            pygame.display.flip()


if __name__ == '__main__':
    #main method, initiate and run the game
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()


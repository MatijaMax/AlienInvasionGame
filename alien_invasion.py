import sys
import pygame
from spaceship import Ship
from alien import Alien
from bullet import Bullet
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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        #load audio
        pygame.mixer.music.load("audio/julia.mp3")
        pygame.mixer.music.set_volume(0.6)
        pygame.mixer.music.play(-1)


    def run_game(self):
        #start the main loop of the game
        pygame.mixer.music.set_endevent(pygame.USEREVENT)  # Music end event
        while True:
            #keyboard and mouse events
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._clean_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.USEREVENT:
                pygame.mixer.music.play(-1)  # Restart the music    
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
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _check_keyup_events(self, event):        
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False   
            elif event.key == pygame.K_q:
                 sys.exit()           

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            new_bullet.bullet_sound.play()

    def _clean_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        
        self.aliens.add(alien)

    def _update_screen(self):
            #redraw screen color
            self.screen.fill(self.bg_color)          
            #redraw screen color bg
            self.screen.blit(self.bg_image, (0, 0))
            #bullets
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            self.ship.blitme()
            self.aliens.draw(self.screen)
            #most recent screen visibility
            pygame.display.flip()


if __name__ == '__main__':
    #main method, initiate and run the game
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()


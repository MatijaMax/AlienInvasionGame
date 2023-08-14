import sys
import pygame
from spaceship import Ship
from alien import Alien
from bullet import Bullet
from settings import Settings
import time

class AlienInvasion:

    def __init__(self):   
        #initialize the game
        pygame.init()
        self.clock = pygame.time.Clock() 
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.boom_sound = pygame.mixer.Sound("audio/boom.wav")
        self.wave_sound = pygame.mixer.Sound("audio/new_wave.wav")
        self.previous_collisions = {} # for the boom sound :)
        # self.screen = pygame.display.set_mode((0, 0) , pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")

        #bg color
        self.bg_color = self.settings.bg_color

        #bg image
        #load and resize
        self.bg_image = pygame.image.load('images/invasion_bg.png')
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
            self._new_fleet()
            self._alien_hit()
            self._update_aliens()
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
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 4 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height    

    def _new_fleet(self):
         if not self.aliens:
              self.wave_sound.play()
              time.sleep(1)
              self.bullets.empty()
              self._create_fleet()
        
    def _create_alien(self, current_x, current_y):
        new_alien = Alien(self)
        new_alien.x = current_x
        new_alien.rect.x = current_x
        new_alien.rect.y = current_y
        self.aliens.add(new_alien)       

    def _check_fleet_edges(self):
         for alien in self.aliens.sprites():
              if alien.check_edges():
                   self._change_fleet_direction()
                   break
              
    def _change_fleet_direction(self):
         for alien in self.aliens.sprites():
              alien.rect.y += self.settings.fleet_drop_speed
         self.settings.fleet_direction *= -1


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

    def _update_aliens(self):
            self._check_fleet_edges()
            self.aliens.update()

    def _alien_hit(self):
        previous_collisions = self.previous_collisions.copy()
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions != previous_collisions:
            self.boom_sound.play()

if __name__ == '__main__':
    #main method, initiate and run the game
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()


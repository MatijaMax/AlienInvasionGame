import sys
import pygame
from spaceship import Ship
from alien import Alien
from bullet import Bullet
from settings import Settings
import time
from game_stats import GameStats
from plasma_ball import Plasma
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:

    def __init__(self):   
        #initialize the game
        pygame.init()
        self.clock = pygame.time.Clock() 
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.boom_sound = pygame.mixer.Sound("audio/boom.wav")
        self.wave_sound = pygame.mixer.Sound("audio/new_wave.wav")
        self.ship_hit = pygame.mixer.Sound("audio/shiphit.mp3")
        self.previous_collisions = {} # for the boom sound :)
        # self.screen = pygame.display.set_mode((0, 0) , pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.game_active = False
        self.play_button = Button(self)
        self.menu_music = True


        #bg color
        self.bg_color = self.settings.bg_color

        #bg image
        #load and resize
        self.bg_image = pygame.image.load('images/invasion_bg.png')
        self.play_bg = pygame.image.load('images/play_bg.jpg')
        self.bg_image = pygame.transform.scale(self.bg_image, (self.settings.screen_width, self.settings.screen_height))
        self.play_bg = pygame.transform.scale(self.play_bg, (self.settings.screen_width, self.settings.screen_height))  
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.plasmas = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        #load audio
        pygame.mixer.music.load("audio/a_bit_of_hope.mp3")
        pygame.mixer.music.set_volume(0.6)
        pygame.mixer.music.play(-1)


    def run_game(self):
        #start the main loop of the game
        pygame.mixer.music.set_endevent(pygame.USEREVENT)  # Music end event
        while True:
            #keyboard and mouse events
            self._check_events()

            if self.game_active:
                self.ship.update()
                self.bullets.update()
                self.plasmas.update()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_high_score()
            self.sb.prep_hearts()
            self.game_active = True
            self.bullets.empty()
            self.aliens.empty()
            self.plasmas.empty()
            self._create_fleet()
            self.settings.initialize_dynamic_settings()
            self.ship.center_ship()
            pygame.mixer.music.load("audio/julia.mp3")
            pygame.mixer.music.set_volume(0.6)
            pygame.mixer.music.play(-1)
            self.menu_music = False
            pygame.mouse.set_visible(False)

    def _play_shortcut(self):
        if not self.game_active:
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_high_score()
            self.sb.prep_hearts()
            self.game_active = True
            self.bullets.empty()
            self.aliens.empty()
            self.plasmas.empty()
            self._create_fleet()
            self.settings.initialize_dynamic_settings()
            self.ship.center_ship()
            pygame.mixer.music.load("audio/julia.mp3")
            pygame.mixer.music.set_volume(0.6)
            pygame.mixer.music.play(-1)
            self.menu_music = False
            pygame.mouse.set_visible(False)

        

    def _check_keydown_events(self, event):        
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()
            elif event.key == pygame.K_p:
                self._play_shortcut()

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
            if self.game_active:
                new_bullet.bullet_sound.play()

    def _clean_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        for plasma in self.plasmas.copy():
            if plasma.rect.bottom <= 0:
                self.plasmas.remove(plasma)

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
              self.settings.increase_speed()
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
            self.sb.show_score()
            for plasma in self.plasmas.sprites():
                plasma.draw_bullet()
            #most recent screen visibility
            if not self.game_active:
                if not self.menu_music:
                    self.menu_music = True
                    pygame.mixer.music.load("audio/a_bit_of_hope.mp3")
                    pygame.mixer.music.set_volume(0.6)
                    pygame.mixer.music.play(-1)
                self.screen.blit(self.play_bg, (0, 0))
                self.play_button.draw_button()

            pygame.display.flip()

    def _update_aliens(self):
            self._check_fleet_edges()
            self.aliens.update()

            if pygame.sprite.spritecollideany(self.ship, self.aliens):
                self._ship_hit()

            self._check_aliens_bottom()

            if pygame.sprite.spritecollideany(self.ship, self.plasmas):
                self._ship_hit_plasma()


    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.ship_hit.play()
            time.sleep(1)
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()
            self.wave_sound.play()
            self.sb.prep_hearts()
            time.sleep(1)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _ship_hit_plasma(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.ship_hit.play()
            time.sleep(1)
            self.bullets.empty()
            self.plasmas.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()
            self.wave_sound.play()
            self.sb.prep_hearts()
            time.sleep(1)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)


    def _alien_hit(self):
        previous_collisions = self.previous_collisions.copy()
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions != previous_collisions:
            self.stats.score += self.settings.alien_points
            self.sb.prep_score()
            self.sb.check_high_score() 
            self.boom_sound.play()
            self.settings.aliens_killed += 1
            # print(self.settings.aliens_killed)


    def _check_aliens_bottom(self):
         for alien in self.aliens.sprites():
              if alien.rect.bottom >= self.settings.screen_height:
                   self._ship_hit()
                   break

if __name__ == '__main__':
    #main method, initiate and run the game
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()


import pygame
import alien
from pygame.sprite import Sprite

class Plasma(Sprite):

    def __init__(self, ai_game, alien):
        super().__init__()
        self.image = pygame.image.load('images/blueball.png')
        self.image = pygame.transform.scale(self.image, (20, 25))
        self.image.set_colorkey((0, 0, 0))  # Set black color as transparent

        if (alien.bill):
            self.image = pygame.image.load('images/bill_comet.png')
            self.image = pygame.transform.scale(self.image, (200, 200))
            self.image.set_colorkey((0, 0, 0))  # Set black color as transparent

        if (alien.sans):
            self.image = pygame.image.load('images/sans_attack.jpg')
            self.image = pygame.transform.scale(self.image, (40, 45))
            self.image.set_colorkey((0, 0, 0))  # Set black color as transparent

        self.rect = self.image.get_rect()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        if(alien.bill):
            self.bullet_sound = pygame.mixer.Sound("audio/bill_shot.wav") 
        elif(alien.sans):
            self.bullet_sound = pygame.mixer.Sound("audio/sans_sound.wav")      
        else:
            self.bullet_sound = pygame.mixer.Sound("audio/lasershot.wav")    
        # self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect = self.image.get_rect()
        

        self.y = float(alien.rect.y)

    def update(self):
        self.y += self.settings.plasma_speed
        self.rect.y = self.y

    def draw_bullet(self):
        # pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)
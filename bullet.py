import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        # self.image = pygame.image.load('images/lasergreen_two.png')
        # self.image = pygame.transform.scale(self.image, (20, 25))
        # self.image.set_colorkey((0, 0, 0))  # Set black color as transparent
        # self.rect = self.image.get_rect()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.bullet_sound = pygame.mixer.Sound("audio/lasershot.wav")   

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        # self.screen.blit(self.image, self.rect)
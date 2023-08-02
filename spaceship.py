import pygame

class Ship:

    def __init__(self, ai_game):
        #init ship
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load image
        self.image = pygame.image.load('images/shipy.png')
        self.image = pygame.transform.scale(self.image, (60, 48))  
        self.rect = self.image.get_rect()

        #reinit ship
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
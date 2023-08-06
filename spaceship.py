import pygame

class Ship:

    def __init__(self, ai_game):
        #init ship
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.movement_speed = ai_game.settings.ship_speed

        #load image
        self.image = pygame.image.load('images/shipy.png')
        self.image = pygame.transform.scale(self.image, (60, 48))  
        self.rect = self.image.get_rect()

        #reinit ship
        self.rect.midbottom = self.screen_rect.midbottom

        #moving flags
        self.moving_right = False
        self.moving_left = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.movement_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.movement_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)
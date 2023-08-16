import pygame

class Button:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/play_one.png')
        self.image_two = pygame.image.load('images/creator.png')
        self.image = pygame.transform.scale(self.image, (500, 170))
        self.image_two = pygame.transform.scale(self.image_two, (1000, 178))
        self.image_two.set_colorkey((255, 255, 255))
        # 2582 width 1200 height
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        self.rect_two = self.image_two.get_rect()
        self.rect_two.midtop = self.screen_rect.midtop


    def draw_button(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image_two, self.rect_two)

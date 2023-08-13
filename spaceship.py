import pygame

class Ship:

    def __init__(self, ai_game):
        #init ship
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.movement_speed = ai_game.settings.ship_speed

        #load image
        self.image = pygame.image.load('images/broship.png')
        self.image = pygame.transform.scale(self.image, (60, 48))  
        self.image.set_colorkey((0, 0, 0))  # Set black color as transparent
        # self.make_black_pixels_transparent()  # Make black pixels transparent
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

    def make_black_pixels_transparent(self):
        # Iterate through every pixel in the image
        for y in range(self.image.get_height()):
            for x in range(self.image.get_width()):
                color = self.image.get_at((x, y))
                if color == (0, 0, 0, 255):  # Check if the pixel is black
                    self.image.set_at((x, y), (0, 0, 0, 0))  # Make it transparent

    def blitme(self):
        self.screen.blit(self.image, self.rect)
import pygame.font

class Scoreboard:

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (235, 216, 52)
        self.font = pygame.font.SysFont(None, 36)
        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.score)
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_image.set_colorkey((0, 0, 0))  # Set black color as transparent
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 15

        self.heart_image = pygame.image.load('images/purple_heart.png')
        self.heart_image = pygame.transform.scale(self.heart_image, (25, 25))
        self.heart_image.set_colorkey((255, 255, 255))
        self.heart_rect = self.score_image.get_rect()
        self.heart_rect.right = self.screen_rect.right - 60
        self.heart_rect.top = 15


    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.heart_image, self.heart_rect)

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
        self.prep_high_score()
        self.prep_hearts()

    def prep_score(self):
        score_str = str(self.stats.score)
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_image.set_colorkey((0, 0, 0))  # Set black color as transparent
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 15

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        self.high_score_image.set_colorkey((0, 0, 0)) 
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 15

    def prep_hearts(self):
        score_str = str(self.stats.ships_left)
        score_str = f"{score_str} x"
        self.lives_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.lives_image.set_colorkey((0, 0, 0))  # Set black color as transparent
        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.right = self.screen_rect.left + 40
        self.lives_rect.top = 15

        self.heart_image = pygame.image.load('images/purple_heart.png')
        self.heart_image = pygame.transform.scale(self.heart_image, (25, 25))
        self.heart_image.set_colorkey((255, 255, 255))
        self.heart_rect = self.lives_image.get_rect()
        self.heart_rect.right = self.screen_rect.left + 78
        self.heart_rect.top = 15

    def show_score(self):
        self.screen.blit(self.lives_image, self.lives_rect)
        self.screen.blit(self.heart_image, self.heart_rect)        
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            with open("game_data/highscore.txt", "w") as file:
                file.write(str(self.stats.score))
from pathlib import Path
class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        path = Path('game_data/highscore.txt')
        try:
            self.high_score = int(path.read_text().strip())
        except:
            self.high_score = 0

    def reset_stats(self):
        self.score = 0
        self.ships_left = self.settings.ship_limit



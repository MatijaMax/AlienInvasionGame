class Settings:

    def __init__(self):

        #core settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 0, 0)

        #bullet settings
        self.bullet_width = 7
        self.bullet_height = 13
        self.bullet_color = (0, 255, 0)
        self.bullets_allowed = 10

        #plasma settings
        self.plasma_speed = 4.0
        self.plasma_width = 27
        self.plasma_height = 33
        self.plasma_color = (0, 255, 0)
        self.plasma_allowed = 13

        #alien settings
        self.fleet_drop_speed = 25
        self.ship_limit = 3

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        #score
        self.aliens_killed = 0

        #dynamo
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 6.5
        self.bullet_speed = 4.5
        self.alien_speed = 1.0
        self.fleet_direction = 1 # (1=right) ((-1)=left)
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *=  self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
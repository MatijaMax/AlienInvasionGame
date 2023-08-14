class Settings:

    def __init__(self):

        #core settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (180, 230, 230)
        self.ship_speed = 10

        #bullet settings
        self.bullet_speed = 9.0
        self.bullet_width = 7
        self.bullet_height = 13
        self.bullet_color = (0, 255, 0)
        self.bullets_allowed = 13

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # (1=right) ((-1)=left)
        
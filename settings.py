class Setting:
    ''' lop de luu tru cac setting cua game'''
    def __init__(self):
        #man hinh
        self.screen_width = 1200
        self.screen_height = 800 
        self.bg_color = (0,0,0)
        self.speed = 1.5
        # bullet setting
        
        self.bullet_speed = 1.5
        self.bullet_width = 1.5
        self.bullet_height = 15
        self.bullet_color = (255,255,00)
        self.bullet_allowed = 5
        #alien setting
        self.alien_speed = 1.5
        self.alien_drop_speed = 10
        self.fleet_direction =1

        #ship setting
        self.ship_limits = 3

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_setting()
    def initialize_dynamic_setting(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction=1
        self.alien_points = 50
    def increase_speed(self):
        ''' increase speed settings and alien point'''
        self.ship_speed *= self.speedup_scale 
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

        


        
        
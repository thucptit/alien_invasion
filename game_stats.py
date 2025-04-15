class GameStats:
    def __init__(self, game):
        self.setting = game.setting
        self.reset_stats()
        self.game_active = False
        self.high_score=0
    def reset_stats(self):
        self.left_ship= self.setting.ship_limits
        self.score =0
        self.level = 0
        

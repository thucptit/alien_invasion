import pygame 
from pygame.sprite import Sprite
from settings import Setting
from ship import Ship
class Bullet(Sprite):
    def __init__(self, game):
        """ create a bullet object at the ship curren position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.setting
        self.color= self.settings.bullet_color
        '''create a bullet rect at (0,0) and then set correct position'''
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height) # the bullet's position depend on ship's position
        self.rect.midtop = game.ship.rect.midtop # the bullet emerge from the top of the ship
        '''store the bullet position as a decimal value'''
        self.y = float(self.rect.y)
    def update(self):
        '''move the bullet up the screen'''
        # update the decimal position of the bullet
        self. y -= self.settings.bullet_speed
        # update the rect position
        self.rect.y = self.y
    def draw_bullet(self):
        '''draw bullet to the screen'''
        glow_rect = pygame.Rect(
        self.rect.x - 2, self.rect.y - 2,
        self.rect.width + 4, self.rect.height + 4
    )
        pygame.draw.rect(self.screen, (255, 255, 150), glow_rect)
        
        # Vẽ đạn chính
        pygame.draw.rect(self.screen, self.color, self.rect)


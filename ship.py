import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, game):
        super().__init__()
        # tao con thuyen va vi tri ban dau
        self.screen= game.screen
        self.screen_rect = game.screen.get_rect()
        # them anh va khoi tao con thuyen nam o duoi sat mep
        self.image= pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.setting=game.setting
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False


    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x += self.setting.speed 
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.speed 
        # cap nhat lai gia tri cho self.rect
        self.rect.x = self.x


    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


        
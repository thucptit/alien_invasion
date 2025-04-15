import pygame
from pygame.sprite import Sprite
from settings import Setting
class Alien(Sprite):
    def __init__(self, game):
        ''' tao the alien va vi tri bat dau cua no'''
        super().__init__()
        self.screen = game.screen
        self.settings = game.setting

        # load the image alien and set its rect attribute
        self.image = pygame.image.load('images/ufo.png')
        self.rect= self.image.get_rect()
        # start each new alien near the top-left of the screen
        self.rect.x= self.rect.width
        self.rect.y= self.rect.height
        #store the alien's exact horizontal position
        self.x = float(self.rect.x)



    def update(self):
        ''' move the alien to the right or left'''
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x


    def check_edges(self):
        '''return true if alien at the end of edges'''
        screen_rect= self.screen.get_rect()
        if (self.rect.right >= screen_rect.right) or (self.rect.left <=0) :
            return True

        
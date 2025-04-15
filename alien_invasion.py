import sys
import pygame
from settings import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.setting = Setting()
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.background= pygame.image.load('images/bg1.jpg')
        self.background = pygame.transform.smoothscale(self.background, (self.setting.screen_width, self.setting.screen_height))
        
        self.ship= Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.create_fleet()
        #tao instance de luu tru game statistics

        self.stats = GameStats(self)
        self.button_play = Button(self,"Play")
        self.sb = Scoreboard(self)


    def create_alien(self, number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)
    def create_fleet(self):
        '''create the fleet of UFO'''
        # Make an UFO
        alien = Alien(self)
        alien_width=alien.rect.width
        alien_height=alien.rect.height
        available_space_y = self.setting.screen_height - (3 * alien_height) - self.ship.rect.height
        number_row = available_space_y = available_space_y // (2 * alien_height)

        available_space_x = self.setting.screen_width - (alien_width)
        number_alien= available_space_x // (2 * alien_width)

        for i in range(number_row):
            for j in range(number_alien):
                self.create_alien(j, i)

    def check_fleet_edges(self):
        for i in self.aliens.sprites():
            if i.check_edges():
                self.change_fleet_direction()
                break
    def change_fleet_direction(self):
        for j in self.aliens.sprites():
            j.rect.y += self.setting.alien_drop_speed
        self.setting.fleet_direction *= -1


    def _update_aliens(self):
        self.check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self.ship_hit()
        self.check_aliens_bottom()
    def ship_hit(self):
        if self.stats.left_ship >0:
            self.stats.left_ship -= 1
            self.sb.prep_ships()
            self.bullets.empty()
            self.aliens.empty()
            self.create_fleet()
            self.ship.center_ship()
            # pause 
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(False)
    def check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for aliens in self.aliens.sprites():
            if (aliens.rect.bottom >= screen_rect.bottom) :
                self.ship_hit()
                break
        


    def _update_screen(self):
        self.screen.blit(self.background, (0,0)) # self.screen.blit(self.background, (0, 0)) neu dung background
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen) # to make UFO appear
        self.sb.show_score()
        if not self.stats.game_active :
            self.button_play.draw_button()
        
        pygame.display.flip() # cap nhat noi dung man hinh


    def _fire_bullet(self):
        '''create a new bullet and add it to group'''
        if (len(self.bullets)<self.setting.bullet_allowed):
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet) 
            
    def _update_bullet(self):
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
        self.check_bullet_collisions()


    def check_bullet_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self.create_fleet()
            self.setting.increase_speed() 
            self.stats.level += 1
            self.sb.prep_level()

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.setting.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.check_high_score()


    def check_keydown_event(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left= True
        elif event.key== pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def check_keyup_event(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left =False


    def check_play_button(self, mouse_pos):
        button_clicked = self.button_play.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.setting.initialize_dynamic_setting()

            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.stats.game_active = True
            self.aliens.empty()
            self.bullets.empty()
            self.create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)


    def check_event(self):
        for event in pygame.event.get(): # lay danh sach tat ca su kien nhu(bam phim, di chuot,...)
            if event.type == pygame.QUIT:
                sys.exit() # thoat chuong trinh khi dong cua so
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)
    
    def run_game(self):
        while True:
            self.check_event()
            if self.stats.game_active:
                self.ship.update()
                self.bullets.update() 
                self._update_bullet()
                self._update_aliens()
            self._update_screen()
        
if __name__ == '__main__': # kiem tra xem chuong trinh co dang chay truc tiep khong
    game = AlienInvasion()
    game.run_game()
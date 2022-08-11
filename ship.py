import pygame
from pygame.sprite import Sprite
class Ship(Sprite) :
    def __init__(self, ai_settings, screen):
        """"Initialize the spacecraft and set its initial position"""
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #Loading spacecraft image and obtaining its external rectangle
        self.image=pygame.image.load("C:/Users/cap/Documents/Visual Studio 2015/alien_invasion/image/ship.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        #Put each new ship in the center of the bottom of the screen
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.center=float(self.rect.centerx)
        #Mobile sign
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """Adjust the position of the spacecraft according to the moving signs"""
        #Update the center value of the ship instead of rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        #according to self.center Update rect object
        self.rect.centerx = self.center
    def blitme (self):
        """Draw the spacecraft at the designated location"""
        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        """Center the ship on the screen"""
        self.center=self.screen_rect.centerx
import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """Represents a single alien human"""
    def __init__(self,ai_settings,screen):
        """Initialize the alien and set its starting position"""
        super(Alien, self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        #Load the alien image and set its rect property
        self.image=pygame.image.load("C:/Users/cap/Documents/Visual Studio 2015/alien_invasion/image/alien_image/alien.bmp")
        self.rect=self.image.get_rect()
        #Each alien was initially near the top left corner of the screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #Store the exact location of Aliens
        self.x=float(self.rect.x)
    def blitme(self):
     """Draw aliens in designated locations"""
     self.screen.blit(self.image,self.rect)
    def check_edges(self):
        """If the alien is on the edge of the screen, go back True"""
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True
    def update(self):
         """Move aliens right"""
         self.x += (self.ai_settings.alien_speed_factor *
                       self.ai_settings.fleet_direction)
         self.rect.x=self.x
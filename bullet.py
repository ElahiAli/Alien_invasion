import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """A class of bullet management for a team of spaceships"""
    def __init__ (self,ai_settings,screen,ship):
        """Create a bullet object where the ship is located"""
        super(Bullet,self).__init__()
        self.screen=screen
        #Create a rectangle representing the bullet at (0.0) and set it in the correct position
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,
                          ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        #Store bullet position in decimal
        self.y=float(self.rect.y)
        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor
    def update(self):
        """Move the bullet up"""
        #Update the small value indicating the bullet position
        self.y-=self.speed_factor
        #Update rectde position of bullet
        self.rect.y=self.y
    def draw_bullet(self):
        """Draw bullets on the screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)
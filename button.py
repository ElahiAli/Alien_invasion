import pygame.font
class Button():
    def __init__(self,ai_settings,screen,msg):
        """Initialize button properties"""
        self.screen=screen
        self.screen_rect=screen.get_rect()
        #Set button size and other properties
        self.width,self.height=200,50
        self.button_color=(1,220,212)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)
        #Create and center the button's rect object
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        #Button labels only need to be created once
        self.prep_msg(msg)
    def prep_msg(self,msg):
        """take msg Render to image and center button"""
        self.msg_image=self.font.render(msg,True,self.text_color,
                                        self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
    def draw_button(self):
        #Draw a color filled button to draw text
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
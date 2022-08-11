import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf
def run_game():
    #Initialize the game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #Create play button
    play_button=Button(ai_settings,screen,"play")
    #Create an instance to store game statistics and create a scoreboard
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)
    ship = Ship(ai_settings,screen)
    bullets=Group()
    aliens=Group()
    #Creating alien groups
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #Start the main cycle of the game
    while True:

        #Monitor keyboard and mouse events
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,
                        aliens,bullets)
        if stats.game_active:
            ship.update()
            #Make the most recently drawn screen visible
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,
                              bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,
                             bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,
                         bullets, play_button)
run_game()

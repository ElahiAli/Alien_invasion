import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """Response key"""
    if event.key == pygame.K_RIGHT :
        # Move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT :
        ship.moving_left = True
    elif event.key==pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
        #Create a bullet and add it to the group bullets
    elif event.key==pygame.K_q:
        sys.exit()
def check_keyup_events(event,ship):
    """Response release"""
    if event.key == pygame.K_RIGHT :
        # Move the ship to the right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT :
        # Move the ship to the left
        ship.moving_left = False
def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    """Corresponding key and mouse events"""
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,
                              ship,aliens,bullets,mouse_x,mouse_y)
def check_play_button(ai_settings,screen,stats,sb,play_button,ship,
                      aliens,bullets,mouse_x,mouse_y):
    """Click on the player play Button to start a new game"""
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #Reset game settings
        ai_settings.initialize_dynamic_settings()
        #hide cursor
        pygame.mouse.set_visible(False)
        #Reset game statistics
        stats.reset_stats()
        stats.game_active=True
        #Reset scoreboard image
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        #Empty alien list and bullet list
        aliens.empty()
        bullets.empty()
        #Create a new group of aliens and center the spacecraft
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
                  play_button):
    """Update screen and switch to new screen"""
    #Redraw the screen every time you cycle
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #Show score
    sb.show_score()
    #If the game is inactive, draw the play button
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """Update the location of bullets and delete the disappeared bullets"""
    #Update bullet position
    bullets.update()
    #Delete bullets that have disappeared
    for bullet in bullets.copy() :
        if bullet.rect.bottom <= 0 :
             bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,
                                  aliens,bullets)

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,
                                  aliens,bullets):
    """In response to a collision between a bullet and an alien"""
    #Delete bullets and aliens in collision
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points*len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
    if len(aliens) == 0 :
        # Delete existing bullets and create a new group of Aliens
        bullets.empty()
        ai_settings.increase_speed()
        #Improve the level
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)
def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullets_allowed :
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    # Move the ship to the left
def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
def get_number_rows(ai_settings,ship_height,alien_height):
    """How many lines of aliens can the screen hold"""
    available_space_y = (ai_settings.screen_height -
                        (3*alien_height)-ship_height)
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    #Create an alien and join the current line
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)
def create_fleet(ai_settings,screen,ship,aliens):
    """Creating aliens"""
    #Create an alien and calculate how many aliens a row can hold
    #Space between aliens is alien width
    alien=Alien(ai_settings,screen)
    number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows=get_number_rows(ai_settings,ship.rect.height,
                                alien.rect.height)
    #Create the first line of Aliens
    for row_number in range(number_rows):
     for alien_number in range(number_aliens_x):
         create_alien(ai_settings,screen,aliens,alien_number,
                      row_number)
def check_fleet_edges(ai_settings,aliens):
    """Take action when an alien reaches the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
def change_fleet_direction(ai_settings,aliens):
    """Move the whole group down and change their direction"""
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """Responding to a spaceship hit by an alien"""
    if stats.ships_left>0:
        #Ship_ left -= 1
        stats.ships_left -= 1
        #Update scoreboard
        sb.prep_ships()
       #Empty alien list and bullet list
        aliens.empty()
        bullets.empty()
        #Create a new group of aliens and put the spacecraft in the center of the bottom of the screen
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
         #suspend
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)
def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """Update the location of all aliens in the alien population"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    #Detect collisions between aliens and spacecraft
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
    check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets)

def check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,
                        bullets):
    """Check if any aliens have reached the bottom of the screen"""
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
         #It's handled like a spaceship hit
         ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
         break
def check_high_score(stats,sb):
    """Check if the new highest score is born"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
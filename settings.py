class Settings():
 """Store the set class of alien invasion"""
 def __init__(self):
    """Initialize game settings"""
    #screen setting
    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = (230, 230, 230)
    #Spaceship setup
    self.ship_limit = 3
    #Bullet setting
    self.bullet_width=3
    self.bullet_height=15
    self.bullet_color=60,60,60
    self.bullets_allowed = 8
    #Alien settings
    self.fleet_drop_speed=10
    #How to speed up the game
    self.speedup_scale=1.1
    #Alien points increase speed
    self.score_scale=1.5
    self.initialize_dynamic_settings()
 def initialize_dynamic_settings(self):
    self.ship_speed_factor = 1.5
    self.bullet_speed_factor = 7
    self.alien_speed_factor = 0.3
    #fleet_ 1 for direction to right, - 1 for left
    self.fleet_direction=1
    #scoring
    self.alien_points=50
 def increase_speed(self):
    """Increase speed settings"""
    self.ship_speed_factor*=self.speedup_scale
    self.bullet_speed_factor*=self.speedup_scale
    self.alien_speed_factor*=self.speedup_scale
    self.alien_points=int(self.alien_points*self.score_scale)
    self.alien_points=int(self.alien_points*self.score_scale)
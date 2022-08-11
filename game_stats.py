class GameStats():
    """Track game statistics"""
    def __init__(self,ai_settings):
        """Initialize statistics"""
        self.ai_settings=ai_settings
        self.reset_stats()
        #Make the game inactive at the beginning
        self.game_active=False
        self.high_score=0
    def reset_stats(self):
        """Initializes statistics that may change during play"""
        self.ships_left=self.ai_settings.ship_limit
        self.score=0
        self.level=0
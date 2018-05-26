class GameStats():
    """跟踪统计信息"""

    def __init__(self, ai_settings):
        """init stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 启动时处于活跃状态
        self.game_active = False

    def reset_stats(self):
        """初始化统计信息（每次重新开始都能初始化，不放在__init__()）"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
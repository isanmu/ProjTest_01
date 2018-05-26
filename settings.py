class Settings():
    """ 存储 “Alien invasion”的所有设置-类"""

    def __init__(self):
        """初始化设置--静态设置"""
        # screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship setting
        # self.ship_speed_factor = 1.5  # 默认1
        self.ship_limit = 3

        # bullet setting
        # self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 230, 0
        self.bullets_allowed = 10

        # speed of alien
        # self.alien_speed_factor = 5
        self.fleet_drop_speed = 10
        # fleet_direction = 1 represent shifting right, -1 represent shifting left
        # self.fleet_direction = 1

        # 节奏加快速度参数
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.fleet_direction = 1

    def increase_speed(self):
        """increase speed setting"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
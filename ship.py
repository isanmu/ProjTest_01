import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """初始化ship及其设置"""
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载ship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()     # image surface的属性rect
        self.screen_rect = screen.get_rect()  # 屏幕矩形存储在self.screen_rect

        # 将ship放置底端中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Adjust the location of ships according to move-flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制ship"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """屏幕居中"""
        self.center = self.screen_rect.centerx
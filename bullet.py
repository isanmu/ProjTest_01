import pygame
from pygame.sprite import Sprite


# 继承Sprite类，使用精灵，将相关元素编组，进而同时操作编组中的所有元素
class Bullet(Sprite):
    """一个对ship发射的bullet进行管理的类"""
    def __init__(self, ai_settings, screen, ship):
        # super(Bullet, self).__init__()  # 调用super继承Sprite
        Sprite.__init__(self)
        self.screen = screen

        # 在（0,0）处创建一个表示bullet的rect，再设置正确位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的bullet位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move up"""
        self.y -= self.speed_factor # upper, y smaller
        self.rect.y = self.y

    def draw_bullet(self):
        """plot bullet in screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
# Package Import-----------
# import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf


def run_game():
    # Init the game
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # create play button
    play_button = Button(ai_settings, screen, "Play")

    # 创建存储统计信息的实例
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Create a ship
    ship = Ship(ai_settings, screen)
    # Create a group to store bullets and aliens
    bullets = Group()
    aliens = Group()
    # Create a alien
    alien = Alien(ai_settings, screen)

    # Create a group aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 设置背景色 变量
    # bg_color_gray = (230, 230, 230)
    # screen.fill(bg_color_gray)

    # loop of the game
    while True:

        gf.check_events(ai_settings, screen, stats, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            # print(len(bullets)) # just for debug(effect performance)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens,
                             bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)


run_game()

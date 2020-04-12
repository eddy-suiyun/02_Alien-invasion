# 主程序文件

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 1.初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 2.开始游戏的主循环
    while True:
        # 监视键盘、鼠标、子弹事件
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)

        # 更新屏幕上的图像，并切换到新屏幕
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()
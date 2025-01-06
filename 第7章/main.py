import pygame
import time
from pygame.locals import *

hero_x = 180
hero_y = 500

def hero_plane(screen, hero):
    global hero_x
    global hero_y

    screen.blit(hero, (hero_x, hero_y))
    
    # 获取键盘按下事件
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                hero_y -= 10
            elif event.key == K_DOWN:
                hero_y += 10
            elif event.key == K_LEFT:
                hero_x -= 10
            elif event.key == K_RIGHT:
                hero_x += 10
            elif event.key == K_SPACE:
                pass


def main():
    # 创建一个窗口
    screen = pygame.display.set_mode((480, 700), 0, 32)

    # 创建一个backgeound变量, 用于存放背景图片信息
    background = pygame.image.load('./第7章/feiji/background.png')
    # 创建一个hero变量, 用于存放英雄飞机图片信息
    hero = pygame.image.load('./第7章/feiji/hero1.png')

    while True:
        # blit方法用于对图片进行粘贴操作
        # 窗口对象.blit(图片, (横坐标, 纵坐标))
        screen.blit(background, (0, 0))
        # 创建一个函数hear_plane, 用于粘贴英雄飞机以及移动飞机
        hero_plane(screen, hero)

        # 为窗口添加一个标题
        pygame.display.set_caption('飞机大战')

        # 刷新窗口, 让图片立即生效
        pygame.display.update()
        # time.sleep(0.1)

if __name__ == "__main__":
    main()
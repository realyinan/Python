import pygame
import time
from pygame.locals import *

hero_x = 150
hero_y = 600

# 弹舱
my_bullet = []

# 加载飞机爆炸的多张图片
a = pygame.image.load('./第7章/feiji/enemy2_down1.png')
b = pygame.image.load('./第7章/feiji/enemy2_down2.png')
c = pygame.image.load('./第7章/feiji/enemy2_down3.png')
d = pygame.image.load('./第7章/feiji/enemy2_down4.png')
e = pygame.image.load('./第7章/feiji/enemy2_down5.png')
f = pygame.image.load('./第7章/feiji/enemy2_down6.png')

# 定义一个列表
blow_up = [a, b, c, d, e, f]

enemy_life = 'live'

enemy_x = 130
enemy_path = 'right'
enemy_num = 0 # 初始值为0, 代表爆炸的第一张图片, 循环时依次累加, 不超过4


def hero_plane(screen, hero, bullet):
    global hero_x
    global hero_y
    global my_bullet

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
                my_bullet.append({'x': hero_x + 32, 'y': hero_y-40})

    for i in my_bullet:
        screen.blit(bullet, (i['x'], i['y']))
        i['y'] -= 40
                
def enemy_plane(screen, enemy):
    global enemy_x
    global enemy_path
    global enemy_life
    global enemy_num

    for bullet in my_bullet:
        if (bullet["x"] >= enemy_x and bullet["x"] <= enemy_x + 165) and (bullet["y"] >= 0 and bullet["y"] <= 265):
            enemy_life = 'dead'

    if enemy_life == 'live':
        screen.blit(enemy, (enemy_x, 10))

        # 添加一个判断语句, 防止飞机越界
        if enemy_x >= 250:
            enemy_path = 'left'
        elif enemy_x <= 0:
            enemy_path = 'right'

        if enemy_path == 'left':
            enemy_x -= 10
        elif enemy_path == 'right':
            enemy_x += 10
    elif enemy_life == 'dead':
        if enemy_num <= 5:
            screen.blit(blow_up[enemy_num], (enemy_x, 10))
            enemy_num += 1



def main():
    # 创建一个窗口
    screen = pygame.display.set_mode((480, 700), 0, 32)

    # 创建一个backgeound变量, 用于存放背景图片信息
    background = pygame.image.load('./第7章/feiji/background.png')
    # 创建一个hero变量, 用于存放英雄飞机图片信息
    hero = pygame.image.load('./第7章/feiji/hero1.png')
    # 创建一个bullet变量, 用于存放子弹图片信息
    bullet = pygame.image.load('./第7章/feiji/bullet.png')
    # 创建一个enemy变量, 用于存放敌机信息
    enemy = pygame.image.load('./第7章/feiji/enemy2.png')


    while True:
        # blit方法用于对图片进行粘贴操作
        # 窗口对象.blit(图片, (横坐标, 纵坐标))
        screen.blit(background, (0, 0))

        # 创建一个函数hear_plane, 用于控制我方飞机
        hero_plane(screen, hero, bullet)
        # 创建一个函数enemy_plane, 用于控制敌机
        enemy_plane(screen, enemy)


        # 为窗口添加一个标题
        pygame.display.set_caption('飞机大战')

        # 刷新窗口, 让图片立即生效
        pygame.display.update()
        time.sleep(0.1)

if __name__ == "__main__":
    main()
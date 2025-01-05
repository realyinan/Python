import pygame
import time

def main():
    # 创建一个窗口
    screen = pygame.display.set_mode((480, 700), 0, 32)
    background = pygame.image.load('./第7章/feiji/background.png')

    # 为窗口添加一个标题
    pygame.display.set_caption('飞机大战')
    screen.blit(background, (0, 0))
    pygame.display.update()
    time.sleep(4)


if __name__ == "__main__":
    main()
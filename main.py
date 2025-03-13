import sys
import pygame

# 初始化
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World:)')
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

# 事件迴圈監聽事件，進行事件處理
while True:
    # 迭代整個事件迴圈，若有符合事件則對應處理
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)

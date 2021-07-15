import sys
import pygame
from pygame.locals import *


'''

white = 255, 255, 255
blue = 0, 0, 255
pygame.init()   # 初始化
screen = pygame.display.set_mode((600,500))
myfont = pygame.font.Font(None,60)
textImage = myfont.render('Hello Pygame', True, white)

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill(blue)
    screen.blit(textImage, (100, 100))
    pygame.display.update()


''' # 创建了一个  窗口 可持续 显示 并有用户反应

'''

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption('Drawing Circles')
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill((0,0,200))

    # draw a circle
    color = 255,255,0
    position = 300,250 # 位置
    radius = 100  # 大小
    width = 10  # 线条的 粗细
    pygame.draw.circle(screen,color,position,radius,width)

    pygame.display.update()

''' # 绘制园





















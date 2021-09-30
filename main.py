"""
空白の明け方が、処理ごとにまとまっててめっちゃ見やすいです！
コメントもガシガシ書いていこう

enemyもの部分も表示してみよう
"""
import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("インベーダーゲーム")
screen.fill((0,0,0))

player = pygame.image.load("player.png")
# enemy = pygame.imageload("enemy.png")

playerX = 200
playerY = 100

# enemyX = 100
# enemyY = 200

running = True

# 特になし。強いて言うなら吉田力という男性がうざかった
while running:
    screen.blit(player,(playerX,playerY))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                screen.fill((255,0,0))
            if event.key == K_LEFT:
                screen.fill((0,255,0))
            if event.key == K_UP:
                screen.fill((0,0,255))
            if event.key == K_DOWN:
                screen.fill((255,255,0))
    pygame.display.update()

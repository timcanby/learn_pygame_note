# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import numpy as np
import cv2

def main():
    pygame.init()
    (w, h) = (500, 637)
    (x, y) = (w / 2, h / 2)
    pygame.display.set_mode((w, h), 0, 32) # window size
    screen = pygame.display.get_surface()
    pygame.display.set_caption("kill the virus") # title
    player = pygame.image.load("virus.jpg").convert_alpha()  # キャラ画像の指定
    img = cv2.imread("virus.jpg")

    rect_player = player.get_rect()
    rect_player.center = (x, y)
    flag=0
    while(True):
        screen.fill((255, 255, 255,))
        if flag:

            screen.fill((255, 255, 255,))
            font = pygame.font.Font('Sledge Rough.otf', 100)
            text = font.render('YOU WIN!!!', True, (0, 0, 0))
            screen.blit(text, (100, 100))
            pygame.time.wait(10)
            pygame.display.update()
        else:
            screen.blit(player, rect_player)
            pygame.time.wait(10)
            pygame.display.update()
            roads = np.random.randint(0, 20, 1)
            roads2 = np.random.randint(0, 20, 1)
            x += roads
            y += roads2
            rect_player.center = (x, y)
            if x > w:
                x = 0
            if y > h:
                y = 0
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                x_mouse, y_mouse = event.pos
                if np.abs(x-x_mouse) <=50 and np.abs(y-y_mouse)<=50:
                    flag=1

            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
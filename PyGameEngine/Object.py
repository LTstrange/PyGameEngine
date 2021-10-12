# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 10:59
# @Author  : LTstrange
import pygame


class Object:
    def __init__(self, size, color):
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect()

    def update(self):
        dest = pygame.mouse.get_pos()
        self.rect.move_ip((dest[0] - self.rect.x, dest[1] - self.rect.y))
        self.rect.center = self.rect.topleft

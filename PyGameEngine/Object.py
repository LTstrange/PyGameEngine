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
        pass

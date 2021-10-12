# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 9:52
# @Author  : LTstrange
import pygame
from .Object import Object


class Scene:
    def __init__(self, game, bg_color):
        self.game = game
        self.background = pygame.Surface(self.game.screen.get_rect()[2:])
        self.background.fill(bg_color)

        self.objects = [Object((10, 10), (255, 128, 128))]

    def update(self):
        for obj in self.objects:
            obj.update()

        self.game.screen.blit(self.background, self.background.get_rect())

        for obj in self.objects:
            self.game.screen.blit(obj.surf, obj.rect)

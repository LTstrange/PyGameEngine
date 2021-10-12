# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 9:52
# @Author  : LTstrange
import pygame
from pygame.color import THECOLORS


class Scene:
    def __init__(self, game, bg_color):
        self.game = game
        self.background = pygame.Surface(self.game.screen.get_rect()[2:])
        self.background.fill(bg_color)

        self.objects = []

    def update(self):
        self.game.screen.blit(self.background, self.background.get_rect())

        for obj in self.objects:
            obj.update()

# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 9:52
# @Author  : LTstrange
import warnings

import pygame
from pygame.sprite import Group, LayeredDirty


class Scene:
    def __init__(self, game, bg_color):
        self.game = game
        self.background = pygame.Surface(self.game.screen.get_rect()[2:])
        self.background.fill(bg_color)

        self.group = LayeredDirty()

        self.set_layout()
        self.set_objects()

        self.group.clear(self.game.screen, self.background)

    def update(self, *args, **kwargs):
        self.group.update(*args, **kwargs)

    def draw(self):
        rects = self.group.draw(self.game.screen)
        return rects

    def set_layout(self):
        warnings.warn("Scene.set_layout function NOT implement!")
    
    def set_objects(self):
        warnings.warn("Scene.set_objects function NOT implement!")

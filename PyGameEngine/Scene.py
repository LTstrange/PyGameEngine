# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 9:52
# @Author  : LTstrange
import warnings

import pygame
from pygame.sprite import Group


class Scene:
    """
    Used to manage all components in a single scene
    """
    def __init__(self, game, bg_color):
        self.game = game
        self.background = pygame.Surface(self.game.screen.get_rect()[2:])
        self.background.fill(bg_color)

        self.group = Group()

        self.set_layout()
        self.set_objects()

    def update(self, *args, **kwargs):
        """
        Used to update every components in this scene
        """
        self.group.update(*args, **kwargs)

    def draw(self):
        self.game.screen.blit(self.background, self.background.get_rect())
        self.group.draw(self.game.screen)

    def set_layout(self):
        warnings.warn("Scene.set_layout function NOT implement!")
    
    def set_objects(self):
        warnings.warn("Scene.set_objects function NOT implement!")

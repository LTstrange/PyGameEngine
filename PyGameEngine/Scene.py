# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 9:52
# @Author  : LTstrange
import pygame
from pygame.sprite import Group


class Scene:
    def __init__(self, game, bg_color):
        self.game = game
        self.background = pygame.Surface(self.game.screen.get_rect()[2:])
        self.background.fill(bg_color)

        self.group = Group()

        self.set_layout()

    def update(self):
        self.group.update()

    def draw(self):
        self.game.screen.blit(self.background, self.background.get_rect())
        self.group.draw(self.game.screen)

    def set_layout(self):
        raise NotImplementedError

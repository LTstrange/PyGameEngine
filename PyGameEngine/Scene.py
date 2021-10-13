# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 9:52
# @Author  : LTstrange
import pygame
from pygame.sprite import Group

from .Object import Button, Mouse


class Scene:
    def __init__(self, game, bg_color):
        self.game = game
        self.background = pygame.Surface(self.game.screen.get_rect()[2:])
        self.background.fill(bg_color)

        self.group = Group()

        self.set_layout()

        self.mouse = Mouse()

    def update(self):
        self.mouse.update()

        self.group.update()

        self.game.screen.blit(self.background, self.background.get_rect())

        self.group.draw(self.game.screen)

    def set_layout(self):
        b = Button((0, 0), (50, 20), 'Click!', self.group)
        b.set_color((255,255,224))

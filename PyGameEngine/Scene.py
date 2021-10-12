# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 9:52
# @Author  : LTstrange
import pygame
from pygame.color import THECOLORS


class Scene:
    def __init__(self, game):
        self.game = game
        self.background = pygame.Surface(self.game.screen.get_rect()[2:])
        self.background.fill(THECOLORS['skyblue'])

    def update(self):
        self.game.screen.blit(self.background, self.background.get_rect())

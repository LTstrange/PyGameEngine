# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 10:59
# @Author  : LTstrange
from typing import Union

import pygame
from pygame.math import Vector2
from pygame.sprite import Sprite, AbstractGroup


class Object(Sprite):
    def __init__(self, game, pos, size, color, group: Union[AbstractGroup, list]):
        if group is list:
            group = group[0]
        super().__init__(group)
        self.game = game
        self.pos = Vector2(pos)

        self._image = pygame.Surface(size)
        self._image.fill(color)
        self._rect = self._image.get_rect()

    def update(self, *args, **kwargs):
        pass

    def handle_input(self, *args, **kwargs):
        pass

    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        self._rect.center = self.pos
        return self._rect

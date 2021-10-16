# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 10:59
# @Author  : LTstrange
import pygame
from pygame.color import THECOLORS
from pygame.math import Vector2
from pygame.sprite import AbstractGroup, DirtySprite


class Object(DirtySprite):
    def __init__(self, pos, size, color, *groups: AbstractGroup):
        super().__init__(*groups)
        self.pos = Vector2(pos)
        self.size = size

        self._image = pygame.Surface(size)
        self._image.fill(color)
        self._rect = self._image.get_rect()

    def update(self, *args, **kwargs):
        pass

    def handle_input(self, *args, **kwargs):
        self.dirty = 1
    
    @property
    def image(self):
        return self._image
    
    @property
    def rect(self):
        self._rect.center = self.pos
        return self._rect


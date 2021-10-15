# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 10:59
# @Author  : LTstrange
import pygame
from pygame.color import THECOLORS
from pygame.sprite import Sprite, AbstractGroup


class Object(Sprite):
    def __init__(self, size, color, *groups: AbstractGroup):
        super().__init__(*groups)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def update(self, *args, **kwargs):
        pass

    def handle_input(self, *args, **kwargs):
        pass


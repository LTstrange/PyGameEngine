# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 10:59
# @Author  : LTstrange
import pygame
from pygame.sprite import Sprite, AbstractGroup


class Object(Sprite):
    def __init__(self, size, color, *groups: AbstractGroup):
        super().__init__(*groups)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def update(self, *args, **kwargs):
        dest = pygame.mouse.get_pos()
        self.rect.move_ip((dest[0] - self.rect.x, dest[1] - self.rect.y))
        self.rect.center = self.rect.topleft

    def handle_input(self, *args, **kwargs):
        pass


class Button(Sprite):
    def __init__(self, pos, size, text, color=None, func=None, *groups: AbstractGroup) -> None:
        super().__init__(*groups)
        self.pos = pos
        self.size = size
        self.text = text
        self.color = color
        self.func = func

        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        self.set_color(color)

    def set_color(self, color):
        self.color = color
        self.image.fill(color)

    def handle_input(self, *args, **kwargs):
        if self.func:
            self.func(*args, **kwargs)
        else:
            print("Being clicked.")

    def update(self, *args, **kwargs):
        pass


class Mouse(Sprite):
    """
    Trace Mouse position use Sprite, make mouse click detection much easier.
    """

    def __init__(self, *groups: AbstractGroup) -> None:
        super().__init__(*groups)

        self.image = pygame.Surface((1, 1))

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

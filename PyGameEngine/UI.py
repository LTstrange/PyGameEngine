# -*- coding: utf-8 -*-
# @Time    : 2021/10/15 18:26
# @Author  : LTstrange
from typing import Union

import pygame
from pygame.color import THECOLORS
from pygame.sprite import AbstractGroup, Sprite


class Button(Sprite):
    def __init__(self, pos, size, color, func, group: Union[AbstractGroup, list], text=None, text_color=None,
                 font: pygame.font.Font = None) -> None:
        if group is list:
            group = group[0]
        super().__init__(group)
        self.pos = pos
        self.size = size
        self.color = color
        self.func = func
        self.text = text
        self.text_color = text_color
        self.font = font if font else pygame.font.SysFont(pygame.font.get_default_font(), int(size[1] * 0.8))

        self._image = pygame.Surface(size)
        self.rect = self._image.get_rect()
        self.rect.topleft = pos

        if self.text:
            self.text_img = self.font.render(self.text, True, self.text_color if self.text_color else (0, 0, 0))
            # default center
            self.text_img_rect = self.text_img.get_rect()
            self.text_img_rect.center = self.rect.center

        self.set_color(color)

    def set_color(self, color):
        self.color = color
        self._image.fill(color)

    def handle_input(self, *args, **kwargs):
        if self.func:
            self.func(*args, **kwargs)
        else:
            print("Being clicked.")

    def update(self, *args, **kwargs):
        pass

    @property
    def image(self):
        img = self._image.copy()
        if self.text:
            img.blit(self.text_img, self.text_img_rect)
        return img


class TextBar(Sprite):
    """
    Changeable TextBar. Display dynamic text.
    """

    def __init__(self, pos, size, group: Union[AbstractGroup, list], bg_color=None, text_color=None,
                 font: pygame.font.Font = None, text_key=None, alias_type=None):
        if group is list:
            group = group[0]
        super().__init__(group)
        self.pos = pos
        self.size = size
        self.bg_color = bg_color if bg_color else (0, 0, 0, 0)
        self.text = None
        self.text_color = text_color if text_color else THECOLORS['black']
        self.font = font if font else pygame.font.SysFont(pygame.font.get_default_font(), int(size[1] * 0.8))
        self.text_key = text_key

        self._image = pygame.Surface(size).convert_alpha()
        self._image.fill(self.bg_color)
        self.rect = self._image.get_rect()
        if alias_type == "center":
            self.rect.center = pos
        else:
            self.rect.topleft = pos

    def set_text(self, text: str):
        self.text = text

    @property
    def image(self):
        img = self._image.copy()
        text_img = self.font.render(self.text, True, self.text_color)
        rect = text_img.get_rect()
        rect.center = img.get_rect().center
        img.blit(text_img, rect)

        return img

    def update(self, *args, **kwargs):
        text = ''
        if self.text_key:
            text = kwargs.get(self.text_key, '')
        self.set_text(text)

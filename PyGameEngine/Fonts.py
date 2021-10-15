# -*- coding: utf-8 -*-
# @Time    : 2021/10/13 22:51
# @Author  : LTstrange


import pygame
from pygame import font


class Fonts:
    def __init__(self):
        self.default_font = pygame.font.SysFont(pygame.font.get_default_font(), 10)
        self.fonts = dict()


    def add_font(self, name, size):
        new_font = pygame.font.SysFont(name, size)
        if name in self.fonts.keys():
            font = self.fonts[name]
            self.fonts[name][size] = new_font
        else:
            self.fonts[name] = {size:new_font}


    def get_font_by_name(self, name=None):
        if name == None:
            return self.default_font
        else:
            print(self.fonts.keys)


if __name__ == "__main__":
    pygame.init()
    fonts = Fonts()
    name = pygame.font.get_default_font()
    print(pygame.font.get_fonts())
    fonts.add_font(name, 20)
    print(fonts.fonts)
    fonts.add_font(name, 30)
    print(fonts.fonts)
    fonts.add_font('piboto', 20)
    print(fonts.fonts)
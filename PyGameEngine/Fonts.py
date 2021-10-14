# -*- coding: utf-8 -*-
# @Time    : 2021/10/13 22:51
# @Author  : LTstrange


import pygame


class Fonts:
    def __init__(self):
        self.default_font = pygame.font.SysFont(pygame.font.get_default_font(), 10)
        self.fonts = []

    def add_font(self, name, size):
        new_font = pygame.font.Font(name, size)
        self.fonts[(name, size)] = new_font

    def get_font_by_name(self, name=None):
        if name == None:
            return self.default_font
        else:
            print(self.fonts.keys)


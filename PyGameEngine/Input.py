# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 10:31
# @Author  : LTstrange
import pygame


class Input:
    def __init__(self, game):
        self.game = game

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

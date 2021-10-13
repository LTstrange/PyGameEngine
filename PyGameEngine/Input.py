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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    sps = pygame.sprite.spritecollide(self.game.scene.mouse, self.game.scene.group, dokill=False)
                    for sp in sps:
                        sp.handle_input()


# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 10:31
# @Author  : LTstrange
import pygame
from pygame.sprite import Sprite, AbstractGroup


class Input:
    def __init__(self, game):
        self.game = game
        self.mouse = Mouse()

    def update(self):
        self.mouse.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    sps = pygame.sprite.spritecollide(self.mouse, self.game.scene.group, dokill=False)
                    for sp in sps:
                        sp.handle_input()


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

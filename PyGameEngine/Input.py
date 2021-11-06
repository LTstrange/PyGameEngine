# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 10:31
# @Author  : LTstrange
import pygame
from pygame.math import Vector2
from pygame.sprite import Sprite, AbstractGroup, Group


class Input:
    def __init__(self, game):
        self.game = game
        self.mouse = Mouse()
        self.axis = Vector2()
        self.hit = Vector2()

    def update(self):
        self.hit = Vector2()
        self.mouse.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    sps = pygame.sprite.spritecollide(self.mouse, Group(self.game.scene.groups), dokill=False)
                    for sp in sps:
                        if hasattr(sp, 'handle_input'):
                            sp.handle_input()

            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_w, pygame.K_UP]:
                    self.axis.y -= 1
                    self.hit.y -= 1
                if event.key in [pygame.K_s, pygame.K_DOWN]:
                    self.axis.y += 1
                    self.hit.y += 1
                if event.key in [pygame.K_a, pygame.K_LEFT]:
                    self.axis.x -= 1
                    self.hit.x -= 1
                if event.key in [pygame.K_d, pygame.K_RIGHT]:
                    self.axis.x += 1
                    self.hit.x = 1
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_w, pygame.K_UP]:
                    self.axis.y -= -1
                if event.key in [pygame.K_s, pygame.K_DOWN]:
                    self.axis.y += -1
                if event.key in [pygame.K_a, pygame.K_LEFT]:
                    self.axis.x -= -1
                if event.key in [pygame.K_d, pygame.K_RIGHT]:
                    self.axis.x += -1


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

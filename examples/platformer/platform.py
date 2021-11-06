# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 16:17
# @Author  : LTstrange

"""
The code is modified from DaFluffyPotato's pygame tutorial, material from DaFluffyPotato's pygame tutorial
"""

import pygame
from pygame.color import THECOLORS
from pygame.math import Vector2
from pygame.sprite import AbstractGroup
from pygame.surface import Surface

from config import *
from PyGameEngine import *


class MenuScene(Scene):
    def __init__(self, game, bg_color):
        super().__init__(game, bg_color)

    def set_layout(self):
        b = Button((0, 0), (200, 50), THECOLORS['yellow'], self.checkout_GameScene, self.groups, text='START')
        b.rect.center = (400, 300)

        TextBar((0, 0), (60, 30), self.groups, text_key='fps')

    def checkout_GameScene(self):
        self.game.scene = GameScene(self.game, BG_COLOR)


class GameScene(Scene):
    def __init__(self, game, bg_color):
        super().__init__(game, bg_color)
        self.tilemap = TileMap((0, 0), (16, 16))
        self.display = Surface((300, 200))

    def set_layout(self):
        TextBar((0, 0), (30, 15), self.groups, text_key='fps')

    def set_objects(self):
        Character(self.game, (50, 50), THECOLORS['red'], self.groups)

    def draw(self):
        self.display.blit(self.background, self.background.get_rect())
        for group in self.groups:
            group.draw(self.display)
        self.game.screen.blit(pygame.transform.scale(self.display, WIN_SIZE), (0, 0))


class Character(Object):
    def __init__(self, game, pos, color, groups: AbstractGroup):
        super().__init__(game, pos, (0, 0), color, groups)
        self.velocity = Vector2()

        self._image = pygame.image.load('player.png')
        self._image.set_colorkey(THECOLORS['white'])
        self.__rect = self._image.get_rect()

    def update(self, *args, **kwargs):
        if self.pos[1] > 200 - self.rect.height:
            self.velocity.y = -abs(self.velocity.y)
        else:
            self.velocity.y += 0.2 * self.game.delta_time * 100
        self.pos += self.velocity * self.game.delta_time * 100

        axis = self.game.input.axis
        self.pos.x += axis.x * self.game.delta_time * 120


class Game:
    """
    Used to switch scenes and control the game.
    """

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(WIN_SIZE)
        self.running = True
        self.Clock = pygame.time.Clock()
        self.delta_time = 0

        self.input = Input(self)
        self.scene = MenuScene(self, BG_COLOR)

    def run(self):
        while self.running:
            self.delta_time = self.Clock.tick() / 1000
            self.input.update()
            fps = f"fps:{int(self.Clock.get_fps())}"
            self.scene.update(fps=fps)

            self.scene.draw()
            pygame.display.flip()


if __name__ == '__main__':
    Game().run()
    pygame.quit()

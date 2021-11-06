# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 10:22
# @Author  : LTstrange

import pygame
from pygame.color import THECOLORS
from pygame.sprite import AbstractGroup

from config import *
from PyGameEngine import *


class MenuScene(Scene):
    def __init__(self, game, bg_color):
        super().__init__(game, bg_color)

    def set_layout(self):
        b = Button((0, 0), (200, 50), THECOLORS['yellow'], self.checkout_GameScene, self.group, text='START')
        b.rect.center = (400, 300)

        TextBar((0, 0), (60, 30), self.group, text_key='fps')

    def checkout_GameScene(self):
        self.game.scene = GameScene(self.game, BG_COLOR)


class GameScene(Scene):
    def __init__(self, game, bg_color):
        super().__init__(game, bg_color)

    def set_layout(self):
        TextBar((0, 0), (60, 30), self.group, text_key='fps')

    def set_objects(self):
        Character(self.game, (200, 200), (10, 10), THECOLORS['red'], self.group)


class Character(Object):
    def __init__(self, game, pos, size, color, *groups: AbstractGroup):
        super().__init__(game, pos, size, color, *groups)
        self.velocity = 100

    def update(self, *args, **kwargs):
        axis = self.game.input.axis if self.game.input.axis.length() == 0 else self.game.input.axis.normalize()
        self.pos.xy += axis * self.velocity * self.game.delta_time / 1000


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
            self.delta_time = self.Clock.tick()
            self.input.update()
            fps = f"fps:{int(self.Clock.get_fps())}"
            self.scene.update(fps=fps)

            self.scene.draw()
            pygame.display.flip()


if __name__ == '__main__':
    Game().run()
    pygame.quit()

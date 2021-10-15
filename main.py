# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 10:22
# @Author  : LTstrange

import pygame
from pygame.color import THECOLORS

from config import *
from PyGameEngine import *


class MenuScene(Scene):
    def __init__(self, game, bg_color):
        super().__init__(game, bg_color)

    def set_layout(self):
        b = Button((0, 0), (200, 50), THECOLORS['yellow'], None, self.group, text='START')
        b.rect.center = (400, 300)

        TextBar((0, 0), (60, 30), self.group, text_key='fps')


class GameScene(Scene):
    def __init__(self, game, bg_color):
        super().__init__(game, bg_color)

    def set_layout(self):
        TextBar((0, 0), (60, 30), self.group, text_key='fps')

    def set_objects(self):
        Object((10, 10), THECOLORS['red'], self.group)


class Game:
    """
    Used to switch scenes and control the game.
    """

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(WIN_SIZE)
        self.running = True

        self.scene = GameScene(self, BG_COLOR)
        self.input = Input(self)

        self.Clock = pygame.time.Clock()

    def run(self):
        while self.running:
            self.Clock.tick()
            self.input.update()
            fps = f"fps:{int(self.Clock.get_fps())}"
            self.scene.update(fps=fps)

            self.scene.draw()
            pygame.display.flip()


if __name__ == '__main__':
    Game().run()
    pygame.quit()

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


class Game:
    """
    Used to switch scenes and control the game.
    """

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(WIN_SIZE)
        self.running = True

        self.scene = MenuScene(self, BG_COLOR)
        self.input = Input(self)

    def run(self):
        while self.running:
            self.scene.update()
            self.input.update()

            self.scene.draw()
            pygame.display.flip()


if __name__ == '__main__':
    Game().run()
    pygame.quit()

# -*- coding: utf-8 -*-
# @Time    : 2021/10/14 17:42
# @Author  : LTstrange


"""
You can view the colors provided by the colors in pyGame
and display their names and values on terminal when you click it.
"""
import pygame
from pygame.color import THECOLORS
from pygame.sprite import AbstractGroup

from PyGameEngine import *


class ColorBlock(Button):
    def __init__(self, pos, size, name, color, *groups: AbstractGroup):
        super().__init__(pos, size, color, None, *groups)
        self.name = name

    def handle_input(self, *args, **kwargs):
        print(f"{self.name}:{self.color}")


class ColorScene(Scene):
    def __init__(self, game, bg_color):
        super().__init__(game, bg_color)

        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 15)

    def set_layout(self):
        colors = list(THECOLORS.keys())
        for j in range(25):
            for i in range(28):
                try:
                    name = colors[j * 28 + i]
                    color = THECOLORS.get(name)
                except IndexError:
                    break

                ColorBlock((i * 10, j * 10), (10, 10), name, color, self.group)


class Game:
    """
    Used to switch scenes and control the game.
    """

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((280, 250))
        self.running = True

        self.scene = ColorScene(self, (0, 0, 0))
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
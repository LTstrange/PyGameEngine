# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 10:22
# @Author  : LTstrange

import pygame
from config import *
from PyGameEngine import *


class Game:
    """
    Used to switch scenes and control the game.
    """
    def __init__(self):
        self.screen = pygame.display.set_mode(WIN_SIZE)
        self.running = True

        self.scene = Scene(self)
        self.input = Input(self)

    def run(self):
        while self.running:
            self.scene.update()
            self.input.update()
            pygame.display.flip()


if __name__ == '__main__':
    Game().run()
    pygame.quit()

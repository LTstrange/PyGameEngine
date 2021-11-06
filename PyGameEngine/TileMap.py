# -*- coding: utf-8 -*-
# @Time    : 2021/10/20 16:59
# @Author  : LTstrange
import pygame
from pygame.color import THECOLORS


class TileMap:
    def __init__(self, pos, tile_size):
        self.pos = pos
        self.tile_map = []
        self.tile_size = tile_size
        self.tile_size = pygame.Rect(0, 0, *tile_size)

        self.tile_mapper = {0: pygame.Surface(tile_size).convert_alpha()}
        img = pygame.Surface(tile_size).convert_alpha()
        img.fill(THECOLORS['red'])
        self.tile_mapper[1] = img

    def load_map(self, path):
        with open(path, 'r') as f:
            data = f.read()
        self.tile_map = [list(row) for row in data.split('\n')]

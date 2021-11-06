# -*- coding: utf-8 -*-
# @Time    : 2021/10/20 16:59
# @Author  : LTstrange
from os import PathLike
from typing import Union, Tuple

import pygame
from pygame.color import THECOLORS
from pygame.math import Vector2
from pygame.rect import Rect
from pygame.surface import Surface


class TileMap:
    def __init__(self, pos, tile_size: Tuple[int, int]):
        self.pos = pos
        self.tile_map = []
        self.tile_size = tile_size

        self.tile_mapper = dict()
        self.scroll = Vector2()

    def load_map(self, path: str):
        with open(path, 'r') as f:
            data = f.read()
        self.tile_map = [list(row) for row in data.split('\n')]

    def add_tile_img(self, key: str, path):
        image = pygame.image.load(path)
        self.tile_mapper[key] = image

    def draw_map(self):
        height = len(self.tile_map)
        width = len(self.tile_map[0])
        image = Surface((self.tile_size[0] * width, self.tile_size[1] * height)).convert_alpha()
        image.fill((0, 0, 0, 0))
        tile_rects = []
        for y, row in enumerate(self.tile_map):
            for x, tile in enumerate(row):
                if tile != '0':
                    tile_rects.append(Rect(x * 16, y * 16, 16, 16))
                    image.blit(self.tile_mapper[tile], (x * self.tile_size[0] - self.scroll.x,
                                                        y * self.tile_size[0] - self.scroll.y))
        return image, tile_rects

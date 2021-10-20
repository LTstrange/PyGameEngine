# -*- coding: utf-8 -*-
# @Time    : 2021/10/20 16:59
# @Author  : LTstrange
import pygame
from pygame.color import THECOLORS


class TileMapper:
    def __init__(self, tile_size):
        self.mapper = {0: pygame.Surface(tile_size).convert_alpha()}
        self.mapper[0].fill((0, 0, 0, 0))

    def add_tile_img(self, key: int, img: pygame.Surface):
        if key:
            self.mapper[key] = img


class TileMap:
    def __init__(self, pos, size, tile_size, mapper: TileMapper):
        self.pos = pos
        self.tile_map = [[0, 1, 0],
                         [1, 0, 1]]
        self.tile_size = tile_size
        self.tile_size = pygame.Rect(0, 0, *tile_size)

        self.tile_mapper = mapper
        img = pygame.Surface(tile_size).convert_alpha()
        img.fill(THECOLORS['red'])
        self.tile_mapper.add_tile_img(1, img)

        self._image = pygame.Surface(size).convert_alpha()
        self._image.fill((0, 0, 0, 0))
        self._rect = self._image.get_rect()
        self._rect.topleft = pos

    @property
    def image(self):
        img = self._image.copy()
        for i, row in enumerate(self.tile_map):
            for j, tile_type in enumerate(row):
                img.blit(self.tile_mapper[tile_type], (j * self.tile_size.width, i * self.tile_size.height))
        return img

    @property
    def rect(self):
        return self._rect

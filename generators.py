import random

from tile import Tile

import search

class EmptyGenerator:

    def generate(self, width, height):
        tiles = []
        for r in range(0, height):
            row = []
            for c in range(0, width):
                row.append(Tile(Tile.EMPTY_CHAR, True))
            tiles.append(row)
        return tiles

class RandomFillGenerator:

    def __init__(self, obstacle_density=0, enemy_density=0):
        self.obstacle_density = min(1.0, obstacle_density)
        self.enemy_density = min(1.0, enemy_density)

    def generate(self, width, height):
        tiles = self.generate_obstacles(width, height)
        tiles = self.generate_enemies(tiles, width, height)
        return tiles

    def generate_obstacles(self, width, height):
        obstacles = int(self.obstacle_density * width * height)
        for attempt in range(0, obstacles):
            tiles = EmptyGenerator.generate(self, width, height)
            for i in range(0, obstacles - attempt):
                rand_r = random.randint(0, height - 1)
                rand_c = random.randint(0, width - 1)
                if self.is_valid_obstacle_location(tiles, rand_r, rand_c):
                    tiles[rand_r][rand_c] = Tile(Tile.OBSTACLE_CHAR, False)
            if search.bfs(tiles):
                return tiles
        return None

    def is_valid_obstacle_location(self, tiles, rand_r, rand_c):
        if rand_r == 0 and rand_c == 0:
            return False
        if rand_r == len(tiles) - 1 and rand_c == len(tiles[0]) - 1:
            return False
        return True

    def generate_enemies(self, tiles, width, height):
        enemies = int(self.enemy_density * width * height)
        for i in range(0, enemies):
            rand_r = random.randint(0, height - 1)
            rand_c = random.randint(0, width - 1)
            if self.is_valid_enemy_location(tiles, rand_r, rand_c):
                tiles[rand_r][rand_c] = Tile(Tile.ENEMY_CHAR, True)
        return tiles

    def is_valid_enemy_location(self, tiles, rand_r, rand_c):
        if rand_r == 0 and rand_c == 0:
            return False
        if rand_r == len(tiles) - 1 and rand_c == len(tiles[0]) - 1:
            return False
        if tiles[rand_r][rand_c].char != Tile.EMPTY_CHAR:
            return False
        return True

from move import Move
from tile import Tile

class Road:

    PLAYER_CHAR = 'I'
    TELOS_CHAR = 'T'
    EMPTY_CHAR = '.'
    VISITED_CHAR = 'x'

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.player_r = 0
        self.player_c = 0

        empty_tile = Tile(self.EMPTY_CHAR, True)
        self.tiles = [[empty_tile for c in range(0, self.width)] for r in range(0, self.height)]
        self.tiles[0][0] = self.PLAYER_CHAR
        self.tiles[-1][-1] = self.TELOS_CHAR

    def vert_boundary(self):
        return '+' + ('-' * self.width) + '+\n'

    def move_player(self, move):

        new_location = (self.player_r, self.player_c)
        if move == Move.UP:
            new_location = (self.player_r - 1, self.player_c)
        elif move == Move.LEFT:
            new_location = (self.player_r, self.player_c - 1)
        elif move == Move.DOWN:
            new_location = (self.player_r + 1, self.player_c)
        elif move == Move.RIGHT:
            new_location = (self.player_r, self.player_c + 1)

        if self.is_valid_player_location(new_location):
            self.tiles[new_location[0]][new_location[1]] = self.PLAYER_CHAR
            self.tiles[self.player_r][self.player_c] = Tile(self.VISITED_CHAR, False)

            self.player_r = new_location[0]
            self.player_c = new_location[1]

        return (self.player_r, self.player_c)

    def is_valid_player_location(self, new_location):
        new_r = new_location[0]
        new_c = new_location[1]

        if new_r < 0 or new_r >= self.height:
            return False
        if new_c < 0 or new_c >= self.width:
            return False

        tile = self.tiles[new_r][new_c]
        if type(tile) == Tile:
            return tile.is_passable()
        return tile in [None, self.TELOS_CHAR]

    def at_telos(self):
        return self.player_r == self.height - 1 and self.player_c == self.width - 1

    def __str__(self):

        road_str = self.vert_boundary()
        for r in range(0, self.height):
            road_str += '|'
            for c in range(0, self.width):
                road_str += str(self.tiles[r][c])
            road_str += '|\n'
        road_str += self.vert_boundary()

        return road_str
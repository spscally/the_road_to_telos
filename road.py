from event import Event
from move import Move
from tile import Tile

class Road:

    def __init__(self, width, height, generator):
        self.width = width
        self.height = height

        self.player_r = 0
        self.player_c = 0

        self.tiles = generator.generate(width, height)

        self.tiles[0][0] = Tile.PLAYER_CHAR
        self.tiles[-1][-1] = Tile.TELOS_CHAR
        self.set_visible_around_player()

    def vert_boundary(self):
        return '+' + ('-' * self.width) + '+\n'

    def move_player(self, move):

        new_r = self.player_r
        new_c = self.player_c

        if move == Move.UP:
            new_r = self.player_r - 1
        elif move == Move.LEFT:
            new_c = self.player_c - 1
        elif move == Move.DOWN:
            new_r = self.player_r + 1
        elif move == Move.RIGHT:
            new_c = self.player_c + 1

        event = Event.NONE
        if self.is_valid_player_location(new_r, new_c):

            if self.tiles[new_r][new_c].char == Tile.ENEMY_CHAR:
                event = Event.FIGHT

            self.tiles[new_r][new_c] = Tile.PLAYER_CHAR
            self.tiles[self.player_r][self.player_c] = Tile(Tile.EMPTY_CHAR, True)

            self.player_r = new_r
            self.player_c = new_c

            self.set_visible_around_player()

        return event

    def is_valid_player_location(self, r, c):
        if self.is_on_road(r, c) == False:
            return False

        tile = self.tiles[r][c]
        if type(tile) == Tile:
            return tile.passable
        return tile in [None, Tile.TELOS_CHAR]

    def is_on_road(self, r, c):
        if r < 0 or r >= self.height:
            return False
        if c < 0 or c >= self.width:
            return False
        return True

    def set_visible_around_player(self):
        for r_delta in [-1, 0, 1]:
            for c_delta in [-1, 0, 1]:
                new_r = self.player_r + r_delta
                new_c = self.player_c + c_delta

                if self.is_on_road(new_r, new_c) == False:
                    continue
                tile = self.tiles[new_r][new_c]
                if type(tile) != Tile:
                    continue
                tile.visible = True

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
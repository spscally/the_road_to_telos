class Road:

    PLAYER_CHAR = 'i'
    TELOS_CHAR = 'T'

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.player_r = 0
        self.player_c = 0

    def vert_boundary(self):
        return '+' + ('-' * self.width) + '+\n'

    def move(self, delta_r, delta_c):
        self.player_r += delta_r
        if self.player_r < 0:
            self.player_r = 0
        elif self.player_r >= self.height:
            self.player_r = self.height - 1

        self.player_c += delta_c
        if self.player_c < 0:
            self.player_c = 0
        elif self.player_c >= self.width:
            self.player_c = self.width - 1

        return (self.player_r, self.player_c)

    def at_telos(self):
        return self.player_r == self.height - 1 and self.player_c == self.width - 1

    def update_row(self, row, col, char):
        """
            row:  str row to update
            col:  column to put desired char at
            char: desired char

            returns updated row as str
        """
        cols = list(row)
        cols[col + 1] = char
        return ''.join(cols)

    def __str__(self):

        road_str = self.vert_boundary()
        road_str += ('|' + ' ' * self.width + '|\n') * self.height
        road_str += self.vert_boundary()

        rows = road_str.split('\n')

        player_row = rows[self.player_r + 1]
        player_row = self.update_row(
            player_row, self.player_c, self.PLAYER_CHAR)
        rows[self.player_r + 1] = player_row

        telos_row = rows[self.height]
        telos_row = self.update_row(telos_row, self.width - 1, self.TELOS_CHAR)
        rows[self.height] = telos_row

        return '\n'.join(rows)

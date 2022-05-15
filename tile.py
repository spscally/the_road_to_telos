class Tile:

    PLAYER_CHAR = 'i'
    TELOS_CHAR = 'T'
    EMPTY_CHAR = ' '
    OBSTACLE_CHAR = 'x'
    ENEMY_CHAR = 'a'
    INVISIBLE_CHAR = '.'

    def __init__(self, char, passable):
        self.char = char
        self.passable = passable
        self.visible = False

    def __str__(self):
        if self.visible:
            return self.char
        return self.INVISIBLE_CHAR
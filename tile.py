class Tile:

    def __init__(self, char, passable):
        self.char = char
        self.passable = passable

    def is_passable(self):
        return self.passable

    def __str__(self):
        return self.char
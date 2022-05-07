from time import sleep

import term

from move import Move

class Game:

    DELAY_MS = 25

    UP_BUTTONS = [b'w', 'w']
    LEFT_BUTTONS = [b'a', 'a']
    DOWN_BUTTONS = [b's', 's']
    RIGHT_BUTTONS = [b'd', 'd']

    def __init__(self, road):
        self.road = road

    def play(self):
        while True:

            term.clear()
            print(self.road)

            if self.road.at_telos():
                return

            char = term.getch()
            if char in self.UP_BUTTONS:
                self.road.move_player(Move.UP)
            elif char in self.LEFT_BUTTONS:
                self.road.move_player(Move.LEFT)
            elif char in self.DOWN_BUTTONS:
                self.road.move_player(Move.DOWN)
            elif char in self.RIGHT_BUTTONS:
                self.road.move_player(Move.RIGHT)

            sleep(self.DELAY_MS / 1000)

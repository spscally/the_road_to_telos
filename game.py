from time import sleep

import term


class Game:

    DELAY_MS = 25

    UP_BUTTON = b'w'
    LEFT_BUTTON = b'a'
    DOWN_BUTTON = b's'
    RIGHT_BUTTON = b'd'

    def __init__(self, road):
        self.road = road

    def play(self):
        while True:

            term.clear()
            print(self.road)

            if self.road.at_telos():
                return

            char = term.getch()
            if char == self.UP_BUTTON:
                self.road.move(-1, 0)
            elif char == self.LEFT_BUTTON:
                self.road.move(0, -1)
            elif char == self.DOWN_BUTTON:
                self.road.move(1, 0)
            elif char == self.RIGHT_BUTTON:
                self.road.move(0, 1)

            sleep(self.DELAY_MS / 1000)

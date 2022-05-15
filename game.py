from time import sleep
import random

import term
import controls

from battleground import Battleground
from event import Event
from enemy import Enemy
from move import Move

class Game:

    DELAY_MS = 25

    def __init__(self, road, player):
        self.road = road
        self.player = player

    def play(self):
        while True:

            term.clear()
            print(self.road)

            if self.road.at_telos():
                return

            char = term.getch()
            event = Event.NONE

            if char in controls.UP_BUTTONS:
                event = self.road.move_player(Move.UP)
            elif char in controls.LEFT_BUTTONS:
                event = self.road.move_player(Move.LEFT)
            elif char in controls.DOWN_BUTTONS:
                event = self.road.move_player(Move.DOWN)
            elif char in controls.RIGHT_BUTTONS:
                event = self.road.move_player(Move.RIGHT)
            elif char in controls.QUIT_BUTTONS:
                print("Bye!")
                exit(0)

            if event == event.FIGHT:
                enemy = Enemy(level=1)
                battleground = Battleground(self.player, enemy)
                win = battleground.fight()
                if win == False:
                    exit(0)

            sleep(self.DELAY_MS / 1000)
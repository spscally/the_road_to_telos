from random import Random
import road
import game
import player

from generators import EmptyGenerator, RandomFillGenerator

player = player.Player(10)
first_road = road.Road(32, 16, RandomFillGenerator(obstacle_density=1, enemy_density=0.25))
telos_game = game.Game(first_road, player)
telos_game.play()

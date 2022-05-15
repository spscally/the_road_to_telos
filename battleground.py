from multiprocessing.connection import wait
import random
from time import sleep

from tile import Tile
import term

import controls

class Battleground():

    PADDING = 3
    BATTLE_SLEEP_MS = 1000

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.is_player_turn = True
        self.screen_width = 9 + 4*self.PADDING + 2*len(str(player.max_health)) + 2*len(str(enemy.max_health))

    def fight(self):
        while True:

            term.clear()
            print(self)

            if self.is_player_turn:
                char = term.getch()
                if char in controls.ATTACK_BUTTONS:
                    damage = self.player.attack + random.randint(0, self.player.luck)
                    damage = min(self.enemy.health, damage)
                    self.display_effect(f"Attacked enemy for {damage} damage!")
                    self.enemy.health -= damage
                    if self.enemy.health <= 0:
                        self.display_effect(f"Battle won!")
                        return True
                    self.is_player_turn = False
                elif char in controls.HEAL_BUTTONS:
                    heal = self.player.faith + random.randint(0, self.player.luck)
                    heal = min(self.player.max_health - self.player.health, heal)
                    self.display_effect(f"Healed for {heal} HP!")
                    self.player.health += heal
                    self.is_player_turn = False
                elif char in controls.QUIT_BUTTONS:
                    print("Bye!")
                    exit(0)

            else:

                sleep(self.BATTLE_SLEEP_MS / 1000)
                self.is_player_turn = True

                damage = self.enemy.attack + random.randint(0, self.enemy.luck)
                damage = min(self.player.health, damage)
                self.display_effect(f"Enemy attacked for {damage} damage!")
                self.player.health -= damage
                if self.player.health <= 0:
                    self.display_effect(f"Game over!")
                    return False
                self.is_player_turn = True

    def vert_boundary(self):
        return "+" + (self.screen_width - 2) * "-" + "+\n"

    def display_effect(self, effect):
        term.clear()
        vert_boundary = "+" + (len(effect) + 2) * "-" + "+\n"
        effect_row = f"| {effect} |\n"
        print(vert_boundary + effect_row + vert_boundary)
        sleep(self.BATTLE_SLEEP_MS / 1000)

    def __str__(self):
        bg_str = self.vert_boundary()

        player_padding = self.PADDING + 1 + len(str(self.player.max_health))
        char_row = "|" + player_padding * " "
        char_row += Tile.PLAYER_CHAR + player_padding * " " + "|"
        enemy_padding = self.PADDING + 1 + len(str(self.enemy.max_health))
        char_row += enemy_padding * " " + Tile.ENEMY_CHAR
        char_row += enemy_padding * " " + "|\n"
        bg_str += char_row

        hp_row = "|" + self.PADDING * " " + "["
        player_hp_str = " " * (len(str(self.player.max_health)) - len(str(self.player.health))) + str(self.player.health)
        hp_row += player_hp_str + "/" + str(self.player.max_health) + "]"
        hp_row += self.PADDING * " " + "|" + self.PADDING * " " + "["
        enemy_hp_str = " " * (len(str(self.enemy.max_health)) - len(str(self.enemy.health))) + str(self.enemy.health)
        hp_row += enemy_hp_str + "/" + str(self.enemy.max_health) + "]"
        hp_row += self.PADDING * " " + "|\n"
        bg_str += hp_row

        bg_str += self.vert_boundary()

        if self.is_player_turn:
            attack_row = f"| {controls.ATTACK_BUTTONS[-1]}) ATTACK"
            attack_row += (self.screen_width - len(attack_row) - 1) * " " + "|\n"
            bg_str += attack_row

            heal_row = f"| {controls.HEAL_BUTTONS[-1]}) HEAL"
            heal_row += (self.screen_width - len(heal_row) - 1) * " " + "|\n"
            bg_str += heal_row
        
        else:
            waiting_row = "| Waiting for enemy..."
            waiting_row += (self.screen_width - len(waiting_row) - 1) * " " + "|\n"
            bg_str += waiting_row

            blank_row = "|" + (self.screen_width - 2) * " " + "|\n"
            bg_str += blank_row

        bg_str += self.vert_boundary()

        return bg_str
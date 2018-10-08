"""
Coding: UTF-8
Author: SkyL
"""
from config import *
from player import *
import game

total_player_num = 10
each_game_num = 20

def main():
    players = []
    for i in range(total_player_num):
        bot = Bot(i, total_player_num)
        players.append(bot)

    for i in range(each_game_num):
        for player_a in players:
            for player_b in players:
                if (player_a.pos != player_b.pos):
                    game.Run(player_a, player_b)

    for i in range(total_player_num):
        print("Player_%d: %d" % (i, players[i].score))

    players[1].print_opp_record()

main()

# -*- coding: utf-8 -*-
# -*- author: SkyL  -*-

from config import *
from player import *
import game
from utils.sort_player import *

total_player_num = 10
each_game_num = 20

def main():
    players = []
    for i in range(10):
        bot = Follower(i, 20)
        players.append(bot)
    for i in range(10):
        bot = Bot(i+10, 20)
        players.append(bot)
    for i in range(each_game_num):
        for player_a in players:
            for player_b in players:
                if (player_a.pos != player_b.pos):
                    game.Run(player_a, player_b)

    for i in range(20):
        print("Player_%d: %d" % (players[i].pos, players[i].score))

    players.sort(key=lambda x: x.score, reverse=True)

    print("----------------")
    for i in range(20):
        print("Player_%d: %d" % (players[i].pos, players[i].score))
    players[12].print_opp_record()

main()

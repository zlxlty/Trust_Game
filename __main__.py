# -*- coding: utf-8 -*-
# -*- author: SkyL  -*-

import tg_game

# total_player_num = 15
# each_game_num = 20

def main():

    players = []

    players = tg_game.Load_Players(players)

    # Run the game between every two players
    tg_game.Run(players)

    # Print all the loggings of opponents
    tg_game.Print_Opp_Logs(players)

    tg_game.Print_My_Logs(players)

    players = tg_game.Sort_Players(players)

    print("----------------")

    tg_game.Print_Scores(players)

main()

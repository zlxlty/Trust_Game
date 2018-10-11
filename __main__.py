# -*- coding: utf-8 -*-
# -*- author: SkyL  -*-

import game

# total_player_num = 15
# each_game_num = 20

def main():

    players = []

    players = game.Load_Players(players)

    # Run the game between every two players
    game.Run(players)

    game.Print_Opp_Logs(players)

    game.Print_My_Logs(players)

    players = game.Sort_Players(players)

    print("----------------")

    game.Print_Scores(players)

main()

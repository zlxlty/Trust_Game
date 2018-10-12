# -*- coding: utf-8 -*-
# -*- author: SkyL  -*-

import tg_game
from tg_config import *

def main():

    players = []

    players = tg_game.Load_Players(players)

    for i in range(game_configs['total_rounds']):
        # Run the game between every two players
        tg_game.Run(players)

        players = tg_game.Sort_Players(players)

        print("--------------%d---------------" % (i+1))

        tg_game.Print_Scores(players)

        # tg_game.Print_My_Logs(players)

        players = tg_game.Update(players)

        players = tg_game.Clear_All_logs(players)

        print("--------------%d---------------\n" % (i+1))


main()

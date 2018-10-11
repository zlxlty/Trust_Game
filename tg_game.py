from tg_config import *
from tg_player import *


def First_Cheat(bot_a, bot_b, score_configs):
    bot_a.score += score_configs['single_cheat']
    bot_a.my_logs[str(bot_b.pos)].append(1)
    bot_a.opp_logs[str(bot_b.pos)].append(0)

    bot_b.score += score_configs['single_trust']
    bot_b.my_logs[str(bot_a.pos)].append(0)
    bot_b.opp_logs[str(bot_a.pos)].append(1)

def Both_Trust(bot_a, bot_b, score_configs):
    bot_a.score += score_configs['both_trust']
    bot_a.my_logs[str(bot_b.pos)].append(0)
    bot_a.opp_logs[str(bot_b.pos)].append(0)

    bot_b.score += score_configs['both_trust']
    bot_b.my_logs[str(bot_a.pos)].append(0)
    bot_b.opp_logs[str(bot_a.pos)].append(0)

def Both_Cheat(bot_a, bot_b, score_configs):
    bot_a.score += score_configs['both_cheat']
    bot_a.my_logs[str(bot_b.pos)].append(1)
    bot_a.opp_logs[str(bot_b.pos)].append(1)

    bot_b.score += score_configs['both_cheat']
    bot_b.my_logs[str(bot_a.pos)].append(1)
    bot_b.opp_logs[str(bot_a.pos)].append(1)

def Load_Players(players):

    for player_type, amount in players_configs.items():

        for i in range(amount):
            player = eval(player_type)(len(players), game_configs['total_player_num'])
            players.append(player)

    return players

def Sort_Players(players):
    players.sort(key=lambda x: x.score, reverse=True)
    return players

def Print_Opp_Logs(players):
    for player in players:
        print("--------opp--------")
        print(player.pos)
        player.print_opp_logs()

def Print_My_Logs(players):
    for player in players:
        print("--------my---------")
        print(player.pos)
        player.print_my_logs()

def Print_Scores(players):
    for i in range(game_configs['total_player_num']):
        players[i].print_score()

def Run(players):

    for i in range(game_configs['each_game_num']):
        for player_a in players:
            for player_b in players:
                if (player_a.pos != player_b.pos):

                    dis_a = player_a.strategy(player_b.pos)
                    dis_b = player_b.strategy(player_a.pos)

                    if (dis_a > dis_b):
                        First_Cheat(player_a, player_b, score_configs)
                    elif (dis_b > dis_a):
                        First_Cheat(player_b, player_a, score_configs)
                    elif (dis_a == dis_b and dis_a == 1):
                        Both_Cheat(player_a, player_b, score_configs)
                    elif (dis_a == dis_b and dis_a == 0):
                        Both_Trust(player_a, player_b, score_configs)

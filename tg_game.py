from tg_config import *
from tg_player import *
import random


def First_Cheat(bot_a, bot_b, score_configs):
    bot_a.score += score_configs['single_cheat']
    bot_a.my_logs[str(bot_b.pos)].append(score_configs['CHEAT'])
    bot_a.opp_logs[str(bot_b.pos)].append(score_configs['TRUST'])

    bot_b.score += score_configs['single_trust']
    bot_b.my_logs[str(bot_a.pos)].append(score_configs['TRUST'])
    bot_b.opp_logs[str(bot_a.pos)].append(score_configs['CHEAT'])

def Both_Trust(bot_a, bot_b, score_configs):
    bot_a.score += score_configs['both_trust']
    bot_a.my_logs[str(bot_b.pos)].append(score_configs['TRUST'])
    bot_a.opp_logs[str(bot_b.pos)].append(score_configs['TRUST'])

    bot_b.score += score_configs['both_trust']
    bot_b.my_logs[str(bot_a.pos)].append(score_configs['TRUST'])
    bot_b.opp_logs[str(bot_a.pos)].append(score_configs['TRUST'])

def Both_Cheat(bot_a, bot_b, score_configs):
    bot_a.score += score_configs['both_cheat']
    bot_a.my_logs[str(bot_b.pos)].append(score_configs['CHEAT'])
    bot_a.opp_logs[str(bot_b.pos)].append(score_configs['CHEAT'])

    bot_b.score += score_configs['both_cheat']
    bot_b.my_logs[str(bot_a.pos)].append(score_configs['CHEAT'])
    bot_b.opp_logs[str(bot_a.pos)].append(score_configs['CHEAT'])

def Load_Players(players):

    for player_type, amount in players_configs.items():

        for i in range(amount):
            player = eval(player_type)(len(players), game_configs['total_player_num'])
            players.append(player)

    return players

def Sort_Players(players):
    random.shuffle(players)
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

def Clear_All_logs(players):

    for player in players:
        player.score = 0
        player.opp_logs = {}
        player.my_logs = {}

        for i in range(game_configs['total_player_num']):
            if i != player.pos:
                player.opp_logs[str(i)] = []
                player.my_logs[str(i)] = []
    return players

def Update(players):

    players = Sort_Players(players)

    update_pos = []

    for i in range(game_configs['update_player_num']):
        temp_loser = players.pop()
        update_pos.append(temp_loser.pos)

    temp_winner = players[0].__class__.__name__
    for i in range(game_configs['update_player_num']):
        player = eval(temp_winner)(update_pos[i], game_configs['total_player_num'])
        players.append(player)

    return players

def Run(players):

    for i in range(game_configs['each_game_num']):
        for player_a in players:
            for player_b in players:
                if (player_a.pos != player_b.pos and \
                len(player_a.opp_logs[str(player_b.pos)]) < game_configs['each_game_num']):

                    dis_a = player_a.strategy(player_b.pos)
                    dis_b = player_b.strategy(player_a.pos)

                    if (dis_a > dis_b):
                        First_Cheat(player_a, player_b, score_configs)
                    elif (dis_b > dis_a):
                        First_Cheat(player_b, player_a, score_configs)
                    elif (dis_a == dis_b and dis_a == score_configs['CHEAT']):
                        Both_Cheat(player_a, player_b, score_configs)
                    elif (dis_a == dis_b and dis_a == score_configs['TRUST']):
                        Both_Trust(player_a, player_b, score_configs)

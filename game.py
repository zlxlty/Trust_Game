from config import *
from player import *


def Single_Cheat(bot_a, bot_b, score_configs):
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


def Run(bot_A, bot_B):
    dis_a = bot_A.strategy(bot_B.pos)
    dis_b = bot_B.strategy(bot_A.pos)

    if (dis_a > dis_b):
        Single_Cheat(bot_A, bot_B, score_configs)
    elif (dis_b > dis_a):
        Single_Cheat(bot_B, bot_A, score_configs)
    elif (dis_a == dis_b and dis_a == 1):
        Both_Cheat(bot_A, bot_B, score_configs)
    elif (dis_a == dis_b and dis_a == 0):
        Both_Trust(bot_A, bot_B, score_configs)

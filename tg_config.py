score_configs = {
    'CHEAT' : 1,
    'TRUST' : 0,
    'single_cheat' : 3,
    'single_trust' : -1,
    'both_trust' : 2,
    'both_cheat' : 0,

}

players_configs = {
    'Bot': 5,
    'Follower': 5,
    'Gambler': 5,
    'Pink': 5,
    'Black': 5,

}



total_num = 0
for v in players_configs.values():
    total_num += v

game_configs = {
    'total_player_num': total_num,
    'each_game_num': 10,
    'update_player_num': 5

}

if __name__ == '__main__':
    for k,v in score_configs.items():
        print(str(k)+":\t"+str(v))

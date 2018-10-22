score_configs = {
    'CHEAT' : 1,
    'TRUST' : -1,
    'single_cheat' : 3,
    'single_trust' : -1,
    'both_trust' : 2,
    'both_cheat' : 0,

}

players_configs = {
    'Bot': 4,
    'Follower': 3,
    'Gambler': 3,
    'Pink': 3,
    'Follower_2': 3,
    'Black': 3,
    'Single_Mind': 3,
    'Sherlock': 3,

}



total_num = 0
for v in players_configs.values():
    total_num += v

game_configs = {
    'total_player_num': total_num,
    'each_game_num': 10,
    'update_player_num': 5,
    'mistake_prob': 0,
    'total_rounds': 20,

}

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

game_configs = {
    'total_player_num': 25,
    'each_game_num': 10,
    
}

if __name__ == '__main__':
    for k,v in score_configs.items():
        print(str(k)+":\t"+str(v))

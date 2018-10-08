score_configs = {
    'CHEAT' : 1,
    'TRUST' : 0,
    'single_cheat' : 3,
    'single_trust' : -1,
    'both_trust' : 2,
    'both_cheat' : 0,
}

if __name__ == '__main__':
    for k,v in score_configs.items():
        print(str(k)+":\t"+str(v))

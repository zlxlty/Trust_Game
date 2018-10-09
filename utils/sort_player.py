def sort_player(player_a, player_b):
    if player_a.score > player_b.score:
        return 1
    elif player_a.score < player_b.score:
        return -1
    else:
        return 0

if __name__ == '__main__':
    a  = [1,4,2,2,5]
    a.sort()
    print(a)

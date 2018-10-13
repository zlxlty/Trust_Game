import numpy as np
from tg_config import *

def random_mistake(origin_func):
    def wrapper(self, *args):
        prob = np.random.randint(100)
        if( prob < game_configs['mistake_prob']):
            origin_result = origin_func(self, *args)
            return -1 * origin_result
        else:
            origin_result = origin_func(self, *args)
            return origin_result

    return wrapper

class Bot(object):
    def __init__(self, pos, total_num):
        self.pos = pos
        self.score = 0
        self.opp_logs = {}
        self.my_logs = {}

        for i in range(total_num):
            if i != self.pos:
                self.opp_logs[str(i)] = []
                self.my_logs[str(i)] = []


    def strategy(self, opp_pos):
        return np.random.randint(2)
        #TODO different strategy can be added here

    def print_score(self):
        print("Player_%d (%s): %d" % (self.pos, self.__class__.__name__, self.score))

    def print_my_logs(self):
        for k,v in self.my_logs.items():
            print('Player_%s: %s' % (k, str(v)))

    def print_opp_logs(self):
        for k,v in self.opp_logs.items():
            print('Player_%s: %s' % (k, str(v)))

class Follower(Bot):

    @random_mistake
    def strategy(self, opp_pos):

        opp_log = self.opp_logs[str(opp_pos)]

        if opp_log:
            return opp_log[-1]
        else:
            return -1

class Follower_2(Bot):

    @random_mistake
    def strategy(self, opp_pos):

        opp_log = self.opp_logs[str(opp_pos)]

        try:
            if opp_log[-1] == opp_log[-2] == 1:
                return 1
            else:
                return -1

        except IndexError:
            return -1

class Gambler(Bot):

    @random_mistake
    def strategy(self, opp_pos):
        if 1 in self.opp_logs[str(opp_pos)]:
            return 1
        else:
            return -1

class Pink(Bot):

    @random_mistake
    def strategy(self, opp_pos):
        return -1

class Black(Bot):

    @random_mistake
    def strategy(self, opp_pos):
        return 1

class Single_Mind(Bot):

    @random_mistake
    def strategy(self, opp_pos):

        opp_log = self.opp_logs[str(opp_pos)]
        my_log = self.my_logs[str(opp_pos)]

        try:
            if opp_log[-1] == -1:
                return my_log[-1]
            else:
                return -1 * my_log[-1]

        except IndexError:
            return -1

class Sherlock(Bot):

    @random_mistake
    def strategy(self, opp_pos):

        trial = [-1, 1, -1, -1]
        opp_log = self.opp_logs[str(opp_pos)]

        if len(opp_log) < 4:
            return trial[len(opp_log)]
        elif 1 in opp_log:
            return opp_log[-1]
        else:
            return 1

import numpy as np

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
    def strategy(self, opp_pos):
        if self.opp_logs[str(opp_pos)]:
            return self.opp_logs[str(opp_pos)][-1]
        else:
            return 0

class Gambler(Bot):
    def strategy(self, opp_pos):
        if 1 in self.opp_logs[str(opp_pos)]:
            return 1
        else:
            return 0

class Pink(Bot):
    def strategy(self, opp_pos):
        return 0

class Black(Bot):
    def strategy(self, opp_pos):
        return 1

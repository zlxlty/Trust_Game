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


    def strategy(self):
        return np.random.randint(2)
        #TODO different strategy can be added here

    def print_score(self):
        print("Player_%d: %d" % self.score)

    def print_opp_record(self):
        for k,v in self.opp_logs.items():
            print('Player_%s: %s' % (k, str(v)))

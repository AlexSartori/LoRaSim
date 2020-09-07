'''
    Simulator.py - Simulate LoRa traffic for different intervals.
    Each interval can be associated to a different Markov model.
    Created by Alessandro Sartori, September 2020.
'''

import random
import matplotlib.pyplot as plt
from LoRaSim.SimIntervals import SimIntervals


class Simulator:
    def __init__(self):
        self.time_ms = 0
        self.intervals = SimIntervals()

    def addInterval(self, model, duration):
        next_start = sum(i.duration for i in self.intervals.getIntervals())
        self.intervals.addInterval(next_start, duration, model)

    def getIntervals(self):
        return self.intervals.getIntervals()

    def run(self):
        data = []

        for idx, i in enumerate(self.getIntervals()):
            print("[*] Interval: {} - Time: {}ms - Model: {}".format(
                idx+1,
                self.time_ms,
                i.model.title
            ))
            res = self.simulateInterval(i)
            data.append(res)

        self.plot(data)

    def simulateInterval(self, interval):
        model = interval.model
        elapsed = 0
        res = []
        state = 0 if random.uniform(0, 1) <= 0.5 else 1

        while elapsed < interval.duration:
            self.time_ms += model.tx_time
            elapsed += model.tx_time

            if state == 0:
                res.append((self.time_ms, False))
                if random.uniform(0, 1) <= model.p01:
                    state = 1
            else:
                res.append((self.time_ms, True))
                if random.uniform(0, 1) <= model.p10:
                    state = 0

        return res

    def plot(self, data):
        p_succ_y = []
        p_succ_x = []
        succ, tot = 0, 0

        for interval in data:
            for i in interval:
                if i[1]:
                    succ += 1
                tot += 1
                p_succ_y.append(succ/tot)

            colors = ['lime' if i[1] else 'r' for i in interval]
            x = [i[0] for i in interval]
            plt.scatter(x, [0]*len(x), c=colors)
            p_succ_x.extend(x)

        plt.plot(p_succ_x, p_succ_y)
        plt.xlabel("Time(ms)")
        plt.ylabel("Success probability")
        plt.show()

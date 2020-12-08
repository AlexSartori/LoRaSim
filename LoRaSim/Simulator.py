'''
    Simulator.py - Simulate LoRa traffic for different intervals.
    Each interval can be associated to a different Markov model.
    Created by Alessandro Sartori, September 2020.
'''

import random
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
        self.time_ms = 0
        data = []

        for idx, i in enumerate(self.getIntervals()):
            print("[*] Interval: {} - Time: {}ms - Model: {}".format(
                idx+1,
                self.time_ms,
                i.model.title
            ))
            res = self.simulateInterval(i)
            data.append((i, res))

        return data

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

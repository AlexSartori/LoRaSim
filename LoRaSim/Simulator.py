'''
    Simulator.py - Simulate LoRa traffic for different intervals.
    Each interval can be associated to a different Markov model.
    Created by Alessandro Sartori, September 2020.
'''

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
        for idx, i in enumerate(self.getIntervals()):
            print("[*] Interval: {} - Time: {}ms - Model: {}".format(
                idx+1,
                self.time_ms,
                i.model.title
            ))
            self.simulateInterval(i)

    def simulateInterval(self, interval):
        self.time_ms += interval.duration
        pass

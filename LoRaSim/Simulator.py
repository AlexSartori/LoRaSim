'''
    Simulator.py - Simulate LoRa traffic for different intervals.
    Each interval can be associated to a different Markov model.
    Created by Alessandro Sartori, September 2020.
'''

from LoRaSim.SimIntervals import SimIntervals


class Simulator:
    def __init__(self):
        self.intervals = SimIntervals()

    def addInterval(self, model, duration):
        self.intervals.addInterval(model, duration)

    def getIntervals(self):
        return self.intervals.getIntervals()

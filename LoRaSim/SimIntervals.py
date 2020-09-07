'''
    SimIntervals.py - Represents a sequence of simulation intervals
    in which a particular Markov Chain is used as model.
    Created by Alessandro Sartori, September 2020.
'''

from LoRaSim.MarkovChain import MarkovChain


class Interval:
    def __init__(self, start_time, duration, model):
        assert isinstance(start_time, int)
        assert isinstance(duration, int)
        assert isinstance(model, MarkovChain)
        self.model = model
        self.duration = duration
        self.start_time = start_time


class SimIntervals:
    def __init__(self):
        self.intervals = []

    def addInterval(self, start_time, duration, model):
        i = Interval(start_time, duration, model)
        self.intervals.append(i)

    def getIntervals(self):
        return self.intervals
        # time = 0
        #
        # for i in self.intervals:
        #     yield (time, i.duration, i.model)
        #     time += i.duration

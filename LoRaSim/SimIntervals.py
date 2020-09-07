'''
    SimIntervals.py - Represents a sequence of simulation intervals
    in which a particular Markov Chain is used as model.
    Created by Alessandro Sartori, September 2020.
'''

from LoRaSim.MarkovChain import MarkovChain


class SimIntervals:
    class Interval:
        def __init__(self, model, duration):
            assert isinstance(model, MarkovChain)
            assert isinstance(duration, int)
            self.model = model
            self.duration = duration

    def __init__(self):
        self.intervals = []

    def addInterval(self, model, duration):
        i = self.Interval(model, duration)
        self.intervals.append(i)

    def getIntervals(self):
        time = 0

        for i in self.intervals:
            yield (time, i.duration, i.model)
            time += i.duration

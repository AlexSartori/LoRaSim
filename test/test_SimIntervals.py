from LoRaSim.MarkovChain import MarkovChain
from LoRaSim.SimIntervals import SimIntervals, Interval


def testInit():
    i = SimIntervals()
    assert isinstance(i.intervals, list)
    assert len(i.intervals) == 0


def testAddInterval():
    model = MarkovChain()
    duration = 1500
    i = SimIntervals()
    i.addInterval(0, duration, model)

    m = i.intervals[0]
    assert isinstance(m, Interval)
    assert m.start_time == 0
    assert m.duration == duration
    assert m.model == model


def testGetIntervals():
    model = MarkovChain()
    i = SimIntervals()
    i.intervals.append(Interval(0, 3125, model))
    i.intervals.append(Interval(3125, 200, model))

    ints = list(i.getIntervals())

    assert isinstance(ints[0], Interval)
    assert ints[0].start_time == 0
    assert ints[0].duration == 3125
    assert ints[0].model == model

    assert isinstance(ints[0], Interval)
    assert ints[1].start_time == 3125
    assert ints[1].duration == 200
    assert ints[1].model == model

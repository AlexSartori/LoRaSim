from LoRaSim.SimInterval import SimInterval


def testInit():
    i = SimInterval()
    assert i.model is None
    assert i.time_length == 0

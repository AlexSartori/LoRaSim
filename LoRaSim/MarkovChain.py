'''
    MarkovChain.py - Represents a Markov chain probability matrix
    with additional attributes (title & description). Data can be
    loaded from a file in .ini format. Any unspecified probability
    will be zero.
    Created by Alessandro Sartori, August 2020
'''


class MarkovChain:
    def __init__(self):
        self.title = ''
        self.description = ''
        self.tx_time = 0
        self.p00 = 0
        self.p01 = 0
        self.p10 = 0
        self.p11 = 0

    def loadFromFile(self, fname):
        for line in open(fname):
            self._parseKeyValueString(line.strip())
        if self.tx_time <= 0:
            raise ValueError("TX time can't be 0")

    def _parseKeyValueString(self, line):
        args = line.split('=', 1)

        if len(args) != 2:
            raise SyntaxError("Not in key=value format: " + line)

        key = args[0].lower().strip()
        val = args[1].strip()

        self._parseKeyValuePair(key, val)

    def _parseKeyValuePair(self, k, v):
        if k == 'p00':
            self.p00 = float(v)
        elif k == 'p01':
            self.p01 = float(v)
        elif k == 'p10':
            self.p10 = float(v)
        elif k == 'p11':
            self.p11 = float(v)
        elif k == 'title':
            self.title = v
        elif k == 'description':
            self.description = v
        elif k == 'tx_time':
            self.tx_time = int(v)
        else:
            raise SyntaxError("Unknown key " + k + " for value " + v)

import os
from LoRaSim.MarkovChain import MarkovChain


def testInit():
    chain = MarkovChain()
    assert chain.p00 == 0
    assert chain.p01 == 0
    assert chain.p10 == 0
    assert chain.p11 == 0
    assert chain.title == ''
    assert chain.description == ''


def testAttributes():
    chain = MarkovChain()
    chain.p00 = 0.8
    chain.p01 = 0.2
    chain.p10 = 0.37
    chain.p11 = 0.63
    chain.title = 'test_title'
    chain.description = 'test_desc'

    assert chain.p00 == 0.8
    assert chain.p01 == 0.2
    assert chain.p10 == 0.37
    assert chain.p11 == 0.63
    assert chain.title == 'test_title'
    assert chain.description == 'test_desc'


def testLoadFromFile():
    chain = MarkovChain()
    fname = 'test_chain.ini'

    with open(fname, 'w') as f:
        f.write('title=DR2\n')
        f.write('description=Datarate #2: SF=10 and BW=125kHz\n')
        f.write('p00=0.80\n')
        f.write('p01=0.20\n')
        f.write('p10=0.37\n')
        f.write('p11=0.63\n')

    chain.loadFromFile(fname)
    os.remove(fname)

    assert chain.p00 == 0.8
    assert chain.p01 == 0.2
    assert chain.p10 == 0.37
    assert chain.p11 == 0.63
    assert chain.title == 'DR2'
    assert chain.description == 'Datarate #2: SF=10 and BW=125kHz'

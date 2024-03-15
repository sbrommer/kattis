from itertools import takewhile, dropwhile


def splitat(pred, xs):
    return list(takewhile(pred, xs)), \
           list(dropwhile(pred, xs))


def piglatin(w):
    fst, snd = splitat(lambda c: c not in 'aeiouy', w)
    fst = fst if fst else ['y']

    return ''.join(snd + fst) + 'ay'


for line in open(0).readlines():
    words = line.split()
    print(' '.join(map(piglatin, words)))

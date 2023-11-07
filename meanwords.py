from itertools import zip_longest


def mean(xs):
    return sum(xs) // len(xs)


def transpose(xxs):
    return [list(filter(lambda x: x, xs))
            for xs in zip_longest(*xxs)]


def average(word):
    return chr(mean(list(map(ord, word))))


_, *words = [w.strip() for w in open(0).readlines()]

print(''.join(map(average, transpose(words))))

from itertools import product


# helper functions
def parseline(line):
    h, m, s = line.split()

    return set(product(parsespec(h, 24), parsespec(m), parsespec(s)))


def parsespec(s, m=60):
    return set(range(m)) if s == '*' else parsecsl(s)


def parsecsl(x):
    return set().union(*[parserange(r) for r in x.split(',')])


def parserange(r):
    r = r.split('-')

    return set(range(int(r[0]), int(r[-1]) + 1))


# solution
n = int(input())
times = [parseline(input()) for _ in range(n)]

n_starts = len(set().union(*times))
n_jobs = sum(map(len, times))

print(n_starts, n_jobs)

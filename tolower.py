from sys import stdin

def solvable_t(t):
    return all(map(str.islower, t[1:]))

def solvable_p(p):
    return all(map(solvable_t, p))

P, T = list(map(int, stdin.readline().split()))
lines = map(str.strip, stdin.readlines())
problems = list(zip(*(lines,) * T))

print(sum(map(solvable_p, problems)))

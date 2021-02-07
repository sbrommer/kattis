from sys import stdin

def readdice():
    (a1, b1, a2, b2) = list(map(int, stdin.readline().split()))
    return ((a1, b1), (a2, b2))

def expected(die):
    return (die[0] + die[1]) / 2

g = sum(map(expected, readdice()))
e = sum(map(expected, readdice()))

if g > e:
    print('Gunnar')
if g < e:
    print('Emma')
if g == e:
    print('Tie')

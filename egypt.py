from sys import stdin

def readints():
    return list(map(int, stdin.readline().split()))

ints = readints()

while ints != [0, 0, 0]:
    c = max(ints)
    a = min(ints)
    b = sum(ints) - (a + c)
    print('right' if a**2 + b**2 == c**2 else 'wrong')
    ints = readints()

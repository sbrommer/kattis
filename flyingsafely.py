from sys import stdin

def readints():
    return tuple(map(int, stdin.readline().split()))

t = int(stdin.readline().strip())

for _ in range(t):
    n, m = readints()

    flights = [set(readints()) for _ in range(m)]
    cities = {1}
    p = 0

    while len(cities) < n:
        for flight in flights:
            if len(cities & flight) == 1:
                cities |= flight
                p += 1

    print(p)

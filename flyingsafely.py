def readints():
    return map(int, input().split())


t = int(input())

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

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    cities = set()
    for _ in range(n):
        cities.add(sys.stdin.readline())

    print(len(cities))

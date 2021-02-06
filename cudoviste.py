from sys import stdin

(r, c) = list(map(int, stdin.readline().split()))

squashes = [0] * 5

city = []

for _ in range(r):
    city.append(stdin.readline()[:-1])

for i in range(r-1):
    for j in range(c-1):
        space = city[i][j:j+2] + city[i+1][j:j+2]

        if '#' not in space:
            squashes[space.count('X')] += 1

for i in range(5):
    print(squashes[i])

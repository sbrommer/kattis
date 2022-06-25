R, C = list(map(int, input().split()))

squashes = [0] * 5

city = [input() for _ in range(R)]

for i in range(R-1):
    for j in range(C-1):
        space = city[i][j]   + city[i][j+1] +\
                city[i+1][j] + city[i+1][j+1]

        squashes[space.count('X')] += '#' not in space

print(*squashes)

def transpose(xxs):
    return list(zip(*xxs))


N, M = map(int, input().split())

grid = transpose(map(sorted, transpose([input() for _ in range(N)])))

print('\n'.join(''.join(line) for line in grid))

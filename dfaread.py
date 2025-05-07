def readints():
    return [*map(int, input().split())]


n, _, s, _ = readints()

Σ = input()
finals = {*readints()}
table = [None] + [readints() for _ in range(n)]

m = int(input())
for _ in range(m):
    state = s
    for symbol in input():
        state = table[state][Σ.index(symbol)]
    print('accept' if state in finals else 'reject')

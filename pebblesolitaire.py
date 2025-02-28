def minmoves(g):
    if '-oo' not in g and 'oo-' not in g:
        return g.count('o')

    m = 12
    for i in range(10):
        if g[i:i+3] == '-oo':
            m = min(m, minmoves(g[:i] + 'o--' + g[i+3:]))
        if g[i:i+3] == 'oo-':
            m = min(m, minmoves(g[:i] + '--o' + g[i+3:]))

    return m


n = int(input())

for _ in range(n):
    game = input()
    print(minmoves(game))

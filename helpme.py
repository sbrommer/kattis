FILES = 'abcdefgh'
RANKS = '87654321'
ORDER = 'KQRBNP'

board = open(0).readlines()
board = board[1::2]
board = [list(line[2::4].strip()) for line in board]

white = []
black = []

for r in range(8):
    for f in range(8):
        p = board[r][f]
        s = p.upper() + FILES[f] + RANKS[r]

        if p.isupper():
            white.append(s)

        if p.islower():
            black.append(s)

white.sort(key=lambda p: (ORDER.index(p[0]),      p[2],  p[1]))
black.sort(key=lambda p: (ORDER.index(p[0]), -ord(p[2]), p[1]))

print('White:', end=' ')
print(*[p[1:] if p[0] == 'P' else p for p in white], sep=',')

print('Black:', end=' ')
print(*[p[1:] if p[0] == 'P' else p for p in black], sep=',')

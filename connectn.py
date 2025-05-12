X, Y, N = map(int, input().split())

board = dict()
for x in range(X):
    for y, c in enumerate(input().split()):
        if c != 'O':
            board[x+y*1j] = c

directions = [-1-1j, -1, -1+1j, -1j, 1j, 1-1j, 1, 1+1j]


def play():
    for p, c in board.items():
        for d in directions:
            if all(board.get(p+d*n) == c for n in range(N)):
                return 'BLUE WINS' if c == 'B' else 'RED WINS'

    return 'NONE'


print(play())

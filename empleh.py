def get_pieces():
    pieces = input()[6:].strip()

    if not pieces:
        return []
    else:
        def add_pawn(p):
            return p if len(p) == 3 else 'P' + p


        return list(map(add_pawn, pieces.split(',')))


# Make empty board
line = '+---' * 8 + '+'
white = '|...|:::' * 4 + '|'
black = '|:::|...' * 4 + '|'
board = list(map(list, [line, white, line, black] * 4 + [line]))


# Get pieces
def lower_piece(p):
    return p[0].lower() + p[1:]


pieces = get_pieces() + list(map(lower_piece, get_pieces()))

# Place pieces on board
for p in pieces:
    x = 2 + 4 * (ord(p[1]) - ord('a'))
    y = 17 - (2 * int(p[2]))

    board[y][x] = p[0]

# Print board
for l in board:
    print(*l, sep='')

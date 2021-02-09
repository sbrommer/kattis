from sys import stdin

def readint():
    return int(stdin.readline())

def readints():
    return list(map(int, stdin.readline().split()))

def mirror(state):
    return list(map(lambda row: row[::-1], state))

def turn(state, cw=True):
    if not cw:
        return turn(turn(turn(state)))

    new_state = []
    for r in range(4):
        row = []
        for c in range(4):
            row.append(state[3-c][r])
        new_state.append(row)
    return new_state

def move(row):
    moved = list(filter(lambda c: c > 0, row)) + [0]
    merged = []
    i = 0
    while i < len(moved) - 1:
        if moved[i] == moved[i+1]:
            merged.append(moved[i] * 2)
            i += 1
        else:
            merged.append(moved[i])
        i += 1
    return merged

def left(state):
    new_state = []
    for row in state:
        row = move(row)
        row += [0] * (4 - len(row))
        new_state.append(row)
    return new_state

def up(state):
    return turn(left(turn(state, False)))

def right(state):
    return mirror(left(mirror(state)))

def down(state):
    return turn(left(turn(state)), False)

moves = [left, up, right, down]

state = []
for _ in range(4):
    state.append(readints())

m = readint()

state = moves[m](state)

for row in state:
    print(' '.join(map(str, row)))

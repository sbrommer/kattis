positions = {['ABCD', 'EFGH', 'IJKL', 'MNO.'][x][y]: (x, y)
             for x in range(4) for y in range(4)}

state = [input() for _ in range(4)]

scatter = 0

for x_state in range(4):
    for y_state in range(4):
        tile = state[x_state][y_state]
        x_solved, y_solved = positions[tile]
        if tile != '.':
            scatter += abs(x_solved - x_state) + abs(y_solved - y_state)

print(scatter)

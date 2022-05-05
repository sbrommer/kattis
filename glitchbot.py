# Read input
x, y = [int(n) for n in input().split()]
n = int(input())
instrs = [input() for _ in range(n)]


# Simulate run
def simulate(instrs):
    pos = (0, 0)
    dir = (0, 1)

    for instr in instrs:
        if instr == 'Forward':
            pos = (pos[0] + dir[0], pos[1] + dir[1])

        elif instr == 'Right':
            dir = (dir[1], -dir[0])

        else:  # instr == 'Left':
            dir = (-dir[1], dir[0])

    return pos


# Try every repair
for i in range(n):
    initial = instrs[i]

    for repair in ['Forward', 'Right', 'Left']:
        if initial != repair:
            instrs[i] = repair

            if simulate(instrs) == (x, y):
                print(i + 1, repair)
                exit()

            instrs[i] = initial

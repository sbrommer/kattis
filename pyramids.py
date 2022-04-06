N = int(open(0).readline())

def blocks(level):
    return (2 * level - 1) ** 2

level = 0

while blocks(level + 1) <= N:
    level += 1
    N -= blocks(level)

print(level)

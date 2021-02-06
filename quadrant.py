import sys

def quadrant(x, y):
    if x > 0:
        if y > 0:
            return 1
        if y < 0:
            return 4
    if x < 0:
        if y < 0:
            return 3
        if y > 0:
            return 2

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

print(quadrant(x, y))

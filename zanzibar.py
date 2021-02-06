import sys

t = int(sys.stdin.readline())

for _ in range(t):
    turtles = list(map(int, sys.stdin.readline().split()[:-1]))

    b = 0
    for i in range(len(turtles)-1):
        b += max(turtles[i+1] - turtles[i] * 2, 0)

    print(b)
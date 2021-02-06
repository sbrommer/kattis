from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    (a, b, c) = list(map(int, stdin.readline().split()))

    if a + b == c:
        print('Possible')
    elif max(a, b) - min(a, b) == c:
        print('Possible')
    elif a * b == c:
        print('Possible')
    elif max(a, b) / min(a, b) == c:
        print('Possible')
    else:
        print('Impossible')

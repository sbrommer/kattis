from sys import stdin

def fraction(n, cs):
    f = 1

    for i in range(n):
        if cs[i] > i + 1:
            return -1

        f = min(f, cs[i] / (i + 1))

    return f

n = int(stdin.readline())
cs = list(map(int, stdin.readline().split()))
cs.sort()

f = fraction(n, cs)

print('impossible' if f < 0 else f)

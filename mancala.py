from sys import stdin

def solve(n):
    bins = [n] + [0] * 80

    while bins[0] != 0:
        e = bins.index(0)

        for i in range(e):
            bins[i] -= 1

        bins[e] = e

    b = max(bins)

    return bins[1:b+1]

p = int(stdin.readline())

for _ in range(p):
    (k, n) = list(map(int, stdin.readline().split()))

    bins = solve(n)
    b = len(bins)

    print(k, b)

    for i in range(0, b, 10):
        print(' '.join(map(str, bins[i:i+10])))

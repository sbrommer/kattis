def readints():
    return map(int, input().split())


def time(N, t, d):
    return N * t + N * (N - 1) // 2 * d


N = int(input())

A = time(N, *readints())
B = time(N, *readints())

print('Alice' if A < B else 'Bob' if B < A else '=')

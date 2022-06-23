ns = [int(n) for n in input().split()]
K = int(input())


def f(n, i=0):
    if not n:
        return 1

    return sum(ns[j] * f(n-1, j+1) for j in range(i, 11 - n))


print(f(K))

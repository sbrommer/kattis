from functools import cache


@cache
def solve(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    return (solve(n-1) + solve(n-2)) % (10**9 + 7)


T = int(input())


for _ in range(T):
    n = int(input())
    for i in range(1, n):
        solve(i)
    print(solve(n))

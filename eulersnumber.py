from functools import cache


@cache
def factorial(n):
    if not n:
        return 1

    return n * factorial(n - 1)


n = int(input())

print(sum(1 / factorial(i) for i in range(n + 1)))

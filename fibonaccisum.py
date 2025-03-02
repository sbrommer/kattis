from functools import cache
from bisect import bisect


# Memorise the Fibonacci sequence.
@cache
def fibonacci(n):
    if n <= 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


fibs = [fibonacci(i) for i in range(50)]

# Solve
x = int(input())
fs = []

while x:
    f = fibs[bisect(fibs, x) - 1]
    fs += [f]
    x -= f

print(*fs[::-1])

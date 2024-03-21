from functools import reduce

N = int(input())

for _ in range(N):
    sexagesimal = [int(n) if n else 0 for n in input().split(',')]

    print(reduce(lambda d, s: d * 60 + s, sexagesimal))
